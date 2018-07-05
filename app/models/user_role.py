from .base_role import BaseRole


class UserRole(BaseRole):
    """
    Normal User Roles

    User role has no permissions over other users comments
    """

    def __init__(self):
        super().__init__(role="normal")
        self._permissions = []
