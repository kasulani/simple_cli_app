"""
Delete a Comment Command. The receiver for this command is
the COMMENTS object in models package
"""
from app.models import COMMENTS
from .abs_command import AbsCommand


class DeleteCommentCommand(AbsCommand):

    _name = "DeleteCommentCommand"

    def execute(self, *args, **kwargs):
        comment_id = kwargs["comment_id"]
        old_comment = COMMENTS[comment_id - 1]
        if 'delete' in kwargs["user"].permissions:  # if user has the permission to delete
            old_comment.owner.comments.remove(comment_id)  # remove the id of the comment
            COMMENTS.remove(old_comment)  # remove the comment from the COMMENTS model
            self._message = "Comment deleted successfully"
        else:
            self._message = "You don't have permission to delete a comment"
            raise PermissionError("You don't have permission to delete a comment")
