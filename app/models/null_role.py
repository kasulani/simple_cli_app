from .base_role import BaseRole
from .permission import NullPermission


class NullRole(BaseRole):
    """
    Null role
    """

    def __init__(self):
        self._role = None
        self._permissions = NullPermission()
