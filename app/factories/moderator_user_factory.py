"""
Factory class for moderator users
"""
from .abs_user_factory import AbsUserFactory
from app.models.moderator_user import ModeratorUser


class ModeratorFactory(AbsUserFactory):

    @classmethod
    def create_user(cls, username="", password=""):
        return ModeratorUser(username, password)
