"""
Login Command. The receiver for this command is
the USERS object in models package
"""
from app.models import USERS
from .abs_command import AbsCommand


class LoginCommand(AbsCommand):

    _name = "LoginCommand"

    def execute(self, *args, **kwargs):
        for user in USERS:
            if user.username == kwargs["username"] and user.password == kwargs["password"]:
                self._message = "User login was successful"
                return True
        self._message = "User login failed"
        raise PermissionError("User login failed")
