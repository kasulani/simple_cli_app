from .base_user import BaseUser
from .admin_role import AdminRole


class AdminUser(BaseUser):
    """
    Admin user class
    """

    def __init__(self, username="", password=""):
        super().__init__(username, password, role=AdminRole())
