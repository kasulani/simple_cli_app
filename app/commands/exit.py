"""
Exit command
"""
from .abs_command import AbsCommand


class ExitCommand(AbsCommand):

    _name = "ExitCommand"

    def execute(self, *args, **kwargs):
        raise SystemExit("Application exiting... good bye!")
