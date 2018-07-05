"""
Command Abstract Base Class
"""
from abc import ABC, abstractmethod


class AbsCommand(ABC):

    _message = ""
    _name = ""

    def __str__(self):
        return self._name

    def __repr__(self):
        return self._name

    @property
    def message(self):
        return self._message

    @abstractmethod
    def execute(self, *args, **kwargs):
        """
        This function returns true if it executes successfully
        :param args:
        :param kwargs:
        :return bool:
        """
        raise NotImplementedError
