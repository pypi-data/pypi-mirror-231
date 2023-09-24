import io
import re
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
        self._headers = headers
        self._raw_body = raw_body

    @property
    def raw(self) -> bytes:
        return self._raw_body

    @property
    def status_code(self) -> int:
        match = re.search(r"\b\d{3}\b", self._headers.split("\n")[0])
        if match:
            return int(match.group(0))
        return -1

    @property
    def headers(self) -> T.Dict[str, str]:
        headers: T.Dict[str, str] = {}
        for line in self._headers.split("\n")[1:]:
            if ":" in line:
                key, value = line.split(":", 1)
                key = key.strip()  # Remove leading/trailing spaces
                value = value.strip()  # Remove leading/trailing spaces
                headers[key] = value

        return headers


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
            buffer.write(f"HTTP/2 {self.response.status_code}\n")
            for k, v in self.response.headers.items():
                buffer.write(f"{k}: {v}\n")
        buffer.write("\n\n")
        if self.response is not None:
            buffer.write(self.response.raw.decode("UTF-8", "ignore"))

        return buffer.getvalue()
