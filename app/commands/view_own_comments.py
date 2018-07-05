"""
View own comment(s) Command. The receiver for this command is
the COMMENTS object in models package
"""
from .abs_command import AbsCommand
from app.models import COMMENTS


class ViewOwnCommentCommand(AbsCommand):

    _name = "ViewOwnCommentCommand"
    _comments = []

    @property
    def comments(self):
        return self._comments

    def execute(self, *args, **kwargs):
        self._comments = []  # clear any previous comments
        owner = kwargs["owner"]
        for comment_id in owner.comments:
            self._comments.append(COMMENTS[comment_id-1].comment)
        self._message = "You have {} comment(s)".format(len(owner.comments))
        return True
