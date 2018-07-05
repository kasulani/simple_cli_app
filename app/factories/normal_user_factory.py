"""
Factory class for normal users
"""
from .abs_user_factory import AbsUserFactory
from app.models.normal_user import NormalUser


class NormalUserFactory(AbsUserFactory):

    @classmethod
    def create_user(cls, username="", password=""):
        return NormalUser(username, password)
