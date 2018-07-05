"""
No command implements the null design pattern
"""
from .abs_command import AbsCommand


class NoCommand(AbsCommand):

    def execute(self, *args, **kwargs):
        self._message = "unknown command"
