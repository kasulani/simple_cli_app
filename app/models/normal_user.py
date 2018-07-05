from .base_user import BaseUser
from .user_role import UserRole


class NormalUser(BaseUser):
    """
    Normal user class
    """

    def __init__(self, username="", password=""):
        super().__init__(username, password, role=UserRole())
