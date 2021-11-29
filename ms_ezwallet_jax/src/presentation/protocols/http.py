from abc import ABCMeta
from typing import Optional


class HttpResponse(metaclass=ABCMeta):
    status_code: int
    body: any


class HttpRequest(metaclass=ABCMeta):
    body: Optional[any]
    params: Optional[any]
