import io
import typing as T
from urllib.parse import urlencode


class Request:
    def __init__(
        self,
        method: str,
        path: str,
        headers: T.Optional[T.Dict[str, str]] = None,
        params: T.Optional[T.Dict[str, T.Any]] = None,
    ):
        self.method = method.upper()
        self.path = self._create_path(path, params)
        self.headers = headers

    def _create_path(self, path: str, params: T.Optional[T.Dict[str, T.Any]]) -> str:
        query_string = ""
        if params is not None:
            query_string = urlencode(params)

        return path if query_string == "" else f"{path}?{query_string}"


class Response:
    def __init__(self, headers: str, raw_body: bytes):
        self.headers = headers
        self.raw_body = raw_body


class RoundTrip:
    def __init__(self, hostname: str, port: int):
        self.hostname = hostname
        self.port = port
        self.request: T.Optional[Request] = None
        self.response: T.Optional[Response] = None

    def set_request(self, request: Request) -> None:
        self.request = request

    def set_response(self, response: Response) -> None:
        self.response = response

    def __str__(self) -> str:
        buffer = io.StringIO()
        if self.response is not None:
            buffer.write(self.response.headers)
        buffer.write("\n\n")
        if self.response is not None:
            buffer.write(self.response.raw_body.decode("UTF-8", "ignore"))

        return buffer.getvalue()
