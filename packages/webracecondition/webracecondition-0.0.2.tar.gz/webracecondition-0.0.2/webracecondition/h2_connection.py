import time
import logging
import typing as T
import socket
from abc import ABC, abstractmethod

import scapy.contrib.http2 as h2
from scapy.data import MTU

from .frames import (
    is_frame_type,
    has_ack_set,
    has_end_stream_set,
    create_settings_frame,
)


class H2Connection(ABC):
    """
    Base class for HTTP/2 connections.
    """

    PREFACE = b"PRI * HTTP/2.0\r\n\r\nSM\r\n\r\n"

    def __init__(self, host: str, port: int) -> None:
        self.host = host
        self.port = port
        self.sock = self._connect()

        self._send_preface()
        self._send_initial_settings()
        self._setup_wait_loop()
        logging.info("Completed HTTP/2 connection setup")

    @abstractmethod
    def _connect(self) -> socket.socket:
        pass

    def close(self) -> None:
        self.sock.close()

    def create_request_frames(
        self,
        method: str,
        path: str,
        stream_id: int,
        headers: T.Optional[T.Dict[str, str]] = None,
        body: T.Optional[bytes] = None,
    ) -> h2.H2Seq:
        """
        Create HTTP/2 frames representing a HTTP request.
        :param method: HTTP request method, e.g. GET
        :param path: request path, e.g. /example/path
        :param stream_id: stream ID to use for this request, e.g. 1
        :param headers: request headers
        :param body: request body
        :return: frame sequence consisting of a single HEADERS frame, potentially followed by CONTINUATION and DATA frames
        """
        header_table = h2.HPackHdrTable()
        req_str = f":method {method}\n:path {path}\n:scheme https\n:authority {self.host}:{self.port}\n"

        if headers is not None:
            req_str += "\n".join(
                map(lambda e: "{}: {}".format(e[0], e[1]), headers.items())
            )

        return header_table.parse_txt_hdrs(
            bytes(req_str.strip(), "UTF-8"), stream_id=stream_id, body=body
        )

    def create_dependant_request_frames(
        self,
        method: str,
        path: str,
        stream_id: int,
        dependency_stream_id: int = 0,
        dependency_weight: int = 0,
        dependency_is_exclusive: bool = False,
        headers: T.Optional[T.Dict[str, str]] = None,
        body: T.Optional[bytes] = None,
    ) -> h2.H2Seq:
        """
        Create HTTP/2 frames representing a HTTP request that depends on another request (stream).
        :param method: HTTP request method, e.g. GET
        :param path: request path, e.g. /example/path
        :param stream_id: stream ID to use for this request, e.g. 1
        :param dependency_stream_id: ID of the stream that this request (stream) will depend upon
        :param dependency_weight: weight of the dependency
        :param dependency_is_exclusive: whether the dependency is exclusive
        :param headers: request headers
        :param body: request body
        :return: frame sequence consisting of a single HEADERS frame, potentially followed by CONTINUATION and DATA frames
        """
        req_frameseq = self.create_request_frames(
            method, path, stream_id, headers, body
        )
        dep_req_frames = []
        for f in req_frameseq.frames:
            if is_frame_type(f, h2.H2HeadersFrame):
                pri_hdr_frame = h2.H2PriorityHeadersFrame()
                pri_hdr_frame.stream_dependency = dependency_stream_id
                pri_hdr_frame.weight = dependency_weight
                pri_hdr_frame.exclusive = 1 if dependency_is_exclusive else 0
                pri_hdr_frame.hdrs = f.hdrs
                dep_req_frames.append(
                    h2.H2Frame(stream_id=f.stream_id, flags=f.flags | {"+"})
                    / pri_hdr_frame
                )
            else:
                dep_req_frames.append(f)

        req_frameseq.frames = dep_req_frames
        return req_frameseq

    def read_answers(self, stream_ids: T.List[int], print_frames: bool = True):
        # The stream variable will contain all read frames
        stream = h2.H2Seq()
        # Number of streams closed by the server
        closed_stream = 0

        logging.info("Read loop starting...")
        while True:
            frames = self._recv_frames()
            if frames.stream_id in stream_ids:
                stream.frames.append(frames)
                if print_frames:
                    stream.show()
                if has_end_stream_set(frames):
                    closed_stream += 1

            if closed_stream >= len(stream_ids):
                break

        # Structure used to store textual representation of the stream headers
        headers: T.Dict[int, str] = {}
        # Structure used to store data from each stream
        data: T.Dict[int, h2.H2Frame] = {}

        srv_tblhdr = h2.HPackHdrTable()
        for frame in stream.frames:
            # If this frame is a header
            if is_frame_type(frame, h2.H2HeadersFrame):
                # Convert this header block into its textual representation.
                headers[frame.stream_id] = srv_tblhdr.gen_txt_repr(frame)
            # If this frame is data
            if is_frame_type(frame, h2.H2DataFrame):
                if frame.stream_id not in data:
                    data[frame.stream_id] = []
                data[frame.stream_id].append(frame)

        return (headers, data)

    def infinite_read_loop(self, print_frames: bool = True) -> None:
        """
        Start an infinite loop that reads and possibly prints received frames.
        :param print_frames: whether to print received frames
        """
        logging.info("Infinite read loop starting...")
        while True:
            frames = self._recv_frames()
            if print_frames:
                for f in frames:
                    logging.info("Read frame:")
                    f.show()

    def send_frames(self, *frames: h2.H2Frame) -> None:
        """
        Send frames on this connection.
        :param frames: 1 or more frames to send
        """
        self._send_frames(*frames)

    def recv_frames(self) -> h2.H2Frame:
        """
        Synchronously receive frames. Block if there aren't any frames to read.
        :return: list of received frames
        """
        return self._recv_frames()

    def _setup_wait_loop(self) -> None:
        server_has_acked_settings = False
        we_have_acked_settings = False

        while not server_has_acked_settings or not we_have_acked_settings:
            frames = self._recv_frames()
            for f in frames:
                if is_frame_type(f, h2.H2SettingsFrame):
                    if has_ack_set(f):
                        logging.info("Server acked our settings")
                        server_has_acked_settings = True
                    else:
                        logging.info("Got server settings, acking")
                        self._ack_settings()
                        we_have_acked_settings = True

    def _ack_settings(self) -> None:
        self._send_frames(create_settings_frame(is_ack=True))
        logging.info("Acked server settings")

    def _send_initial_settings(self) -> None:
        settings = [
            h2.H2Setting(id=h2.H2Setting.SETTINGS_ENABLE_PUSH, value=0),
            h2.H2Setting(
                id=h2.H2Setting.SETTINGS_INITIAL_WINDOW_SIZE, value=2_147_483_647
            ),
            h2.H2Setting(id=h2.H2Setting.SETTINGS_MAX_CONCURRENT_STREAMS, value=1000),
        ]
        self._send_frames(create_settings_frame(settings))
        logging.info("Sent settings")

    def _send_frames(self, *frames: h2.H2Frame) -> None:
        b = bytes()
        for f in frames:
            b += bytes(f)
        self._send(b)

    def _send_preface(self) -> None:
        self._send(self.PREFACE)

    def _send(self, bytez) -> None:
        self.sock.send(bytez)

    def _recv_frames(self) -> h2.H2Frame:
        chunk = self._recv()
        return chunk

    def _recv(self) -> bytes:
        while True:
            try:
                return self.sock.recv(MTU)
            except AssertionError:
                # Frame parsing failed on current data, try again in 100 ms
                time.sleep(0.1)
