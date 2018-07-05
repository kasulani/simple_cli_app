from .base_role import BaseRole
from .permission import Permission


class ModeratorRole(BaseRole):
    """
    Moderator role

    The moderator can only delete comments that belong to other users
    """

    def __init__(self):
        super().__init__(role="moderator")
        self._permissions = [Permission("delete")]
