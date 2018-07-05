from abc import ABC, abstractmethod


class AbsUser(ABC):

    @property
    @abstractmethod
    def username(self):
        raise NotImplementedError

    @username.setter
    @abstractmethod
    def username(self, username):
        raise NotImplementedError

    @property
    @abstractmethod
    def password(self):
        raise NotImplementedError

    @password.setter
    @abstractmethod
    def password(self, password):
        raise NotImplementedError

    @property
    @abstractmethod
    def role(self):
        raise NotImplementedError

    @role.setter
    @abstractmethod
    def role(self, role):
        raise NotImplementedError

    @property
    @abstractmethod
    def permissions(self):
        raise NotImplementedError
