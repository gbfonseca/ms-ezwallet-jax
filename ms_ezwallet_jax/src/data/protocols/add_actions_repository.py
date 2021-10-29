from abc import ABCMeta, abstractmethod


class AddActionsRepository(metaclass=ABCMeta):
    @property
    @abstractmethod
    def add(data: list): raise NotImplementedError
