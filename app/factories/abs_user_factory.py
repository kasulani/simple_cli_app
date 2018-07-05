"""
Abstract Base Class for the user factory
"""
from abc import ABC, abstractmethod


class AbsUserFactory(ABC):

    @classmethod
    @abstractmethod
    def create_user(cls, username="", password=""):
        raise NotImplementedError
