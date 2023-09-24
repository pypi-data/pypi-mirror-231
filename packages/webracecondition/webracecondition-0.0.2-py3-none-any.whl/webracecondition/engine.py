import time
import typing as T
from urllib.parse import urlparse
import scapy.contrib.http2 as scapy

from .frames import create_ping_frame
from .h2_tls_connection import H2TLSConnection
from .roundtrip import Request, Response, RoundTrip


class Engine:
    def __init__(self, base_url: str):
        parsed_url = urlparse(base_url)
        assert parsed_url.scheme == "https", "Only HTTP/2 over TLS is supported"
        assert parsed_url.hostname != None, "Hostname cannot be empty"
        
        self._hostname = parsed_url.hostname
        self._port = 443 if parsed_url.port is None else parsed_url.port
        self._requests: T.List[Request] = []

    def add_request(self, req: Request) -> None:
        self._requests.append(req)

    def last_frame_sync_attack(self, print_frames: bool = False) -> T.List[RoundTrip]:
        conn = H2TLSConnection(self._hostname, self._port)

        final_frames = []
        round_trips: T.Dict[int, RoundTrip] = {}

        for idx, req in enumerate(self._requests):
            # Generate a valid client-side stream ID: positive odd integer.
            stream_id = self.generate_stream_id(idx)

            round_trips[stream_id] = RoundTrip(self._hostname, self._port)
            round_trips[stream_id].set_request(req)

            rframe = conn.create_request_frames(
                req.method, req.path, stream_id, headers=req.headers
            )
            # Remove END_STREAM flag from latest frames
            rframe.frames[len(rframe.frames)-1].flags.remove("ES")
            # Send the request frames
            conn.send_frames(rframe)
            # Create the final DATA frame using scapy and store it
            final_frames.append(
                scapy.H2Frame(flags={"ES"}, stream_id=stream_id) / scapy.H2DataFrame()
            )

        # Sleep a little to make sure previous frames have been delivered
        time.sleep(100 / 1000)
        # Send a ping packet to warm the local connection.
        conn.send_frames(create_ping_frame())
        # Send the final frames to complete the requests
        conn.send_frames(*final_frames)

        # Listening for the answers on the connection
        (headers, data) = conn.read_answers(
            list(round_trips.keys()), print_frames=print_frames
        )

        conn.close()

        for id in round_trips.keys():
            raw_body = b""
            for frgmt in data[id]:
                raw_body += frgmt.payload.data

            round_trips[id].set_response(Response(headers[id], raw_body))

        return list(round_trips.values())
    
    def generate_stream_id(self, idx: int) -> int:
        return 2 * idx + 1
