"""
Create a User Command. The receiver for this command is
the USERS object in models package
"""
from app.factories import load_user_factory
from app.models import USERS
from .abs_command import AbsCommand


class CreateUserCommand(AbsCommand):

    _name = "CreateUserCommand"

    def execute(self, *args, **kwargs):
        # todo: check if username is already taken
        factory = load_user_factory(kwargs["role"] + "_user_factory")
        USERS.append(factory.create_user(kwargs["username"], kwargs["password"]))
        self._message = "User created successfully"
        return True
