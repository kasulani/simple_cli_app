from .base_role import BaseRole
from .permission import Permission


class AdminRole(BaseRole):
    """
    Admin role

    The admin can delete and edit comments of other users
    """

    def __init__(self):
        super().__init__(role="admin")
        self._permissions = [Permission("edit"), Permission("delete")]
