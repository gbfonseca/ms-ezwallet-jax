from abc import ABCMeta, abstractmethod
from typing import TypeVar, Generic

T = TypeVar('T')


class HttpClient(metaclass=ABCMeta):
    @property
    @abstractmethod
    def get(self, url: str) -> Generic[T]: raise NotImplementedError
