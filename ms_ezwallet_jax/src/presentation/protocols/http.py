from abc import ABCMeta


class HttpResponse(metaclass=ABCMeta):
    status_code: int
    body: any
