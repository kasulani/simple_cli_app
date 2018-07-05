from .base_user import BaseUser
from .moderator_role import ModeratorRole


class ModeratorUser(BaseUser):
    """
    Moderator user class
    """

    def __init__(self, username="", password=""):
        super().__init__(username, password, role=ModeratorRole())
