"""
Factory class for admin users
"""
from .abs_user_factory import AbsUserFactory
from app.models.admin_user import AdminUser


class AdminFactory(AbsUserFactory):

    @classmethod
    def create_user(cls, username="", password=""):
        return AdminUser(username, password)
