"""
Abstract Base Class for permissions
"""
from abc import ABC, abstractmethod


class AbsPermission(ABC):

    @property
    @abstractmethod
    def permission(self):
        raise NotImplementedError
