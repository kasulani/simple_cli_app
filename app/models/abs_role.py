from abc import ABC, abstractmethod


class AbsRole(ABC):

    @property
    @abstractmethod
    def permissions(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def role(self):
        raise NotImplementedError
