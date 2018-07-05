"""
Factory class for null users
"""
from .abs_user_factory import AbsUserFactory
from app.models.null_user import NullUser


class NormalUserFactory(AbsUserFactory):

    @classmethod
    def create_user(cls, username="", password=""):
        return NullUser()
