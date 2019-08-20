from requests import ConnectionError
from requests import HTTPError
from requests import Timeout
from requests.models import Response

from time import sleep

from typing import Callable
from typing import Dict  # noqa: F401
from typing import Optional


class TimeoutException(Exception):
    pass


def send_request(method: Callable[..., Response],
                 url: str,
                 data: Optional[str] = None,
                 headers: Optional[Dict[str, str]] = None,
                 max_retries: Optional[int] = 1,
                 connection_timeout_seconds: Optional[int] = 3,
                 read_timeout_seconds: Optional[int] = 10,
                 ) -> Response:
    _retries = 1 if (not max_retries or max_retries < 0) else max_retries
    _ctime = 10 if (not connection_timeout_seconds or connection_timeout_seconds < 0) else connection_timeout_seconds
    _rtime = 30 if (not read_timeout_seconds or read_timeout_seconds < 0) else read_timeout_seconds
    for retry_countdown in range(_retries, 0, -1):
        try:
            r: Response = method(url=url, data=data, headers=headers, timeout=(_ctime, _rtime))
            r.raise_for_status()
            break
        except (ConnectionError, Timeout, HTTPError) as e:
            if retry_countdown == 1:
                raise TimeoutException() from e
            else:
                sleep(1.0)
                continue  # TODO: Log?
    return r
