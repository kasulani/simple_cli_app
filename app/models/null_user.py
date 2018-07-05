from .base_user import BaseUser
from .null_role import NullRole


class NullUser(BaseUser):
    """
    Null user class
    """

    def __init__(self):
        self._username = None
        self._password = None
        self._role = NullRole
