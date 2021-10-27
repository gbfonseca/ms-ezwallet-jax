from abc import ABCMeta, abstractmethod


class Controller(metaclass=ABCMeta):
    @property
    @abstractmethod
    def handle(self, http_request): raise NotImplementedError


