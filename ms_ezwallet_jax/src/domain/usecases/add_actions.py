from abc import ABCMeta, abstractmethod


class AddActions(metaclass=ABCMeta):
    @property
    @abstractmethod
    def add(data: list): raise NotImplementedError
