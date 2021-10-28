from abc import ABCMeta, abstractmethod


class DataManipulation(metaclass=ABCMeta):
    @property
    @abstractmethod
    def to_dict(data: str): raise NotImplementedError
