"""
Edit a Comment Command. The receiver for this command is
the COMMENTS object in models package
"""
from app.models import COMMENTS
from .abs_command import AbsCommand


class EditCommentCommand(AbsCommand):

    _name = "EditCommentCommand"

    @staticmethod
    def _is_owner(comment=None, owner=None):
        return comment.owner.username == owner.username

    def execute(self, *args, **kwargs):
        comment_id = kwargs["comment_id"]
        old_comment = COMMENTS[comment_id - 1]
        if 'edit' in kwargs["user"].permissions or self._is_owner(old_comment, kwargs["user"]):
            old_comment.comment = kwargs["new_comment"]
            self._message = "Comment edited successfully"
        else:
            self._message = "You don't have permission to edit a comment"
            raise PermissionError("You don't have permission to edit a comment")
