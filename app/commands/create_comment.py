"""
Create a Comment Command. The receiver for this command is
the COMMENTS object in models package
"""
from .abs_command import AbsCommand
from app.models import COMMENTS
from app.models.comment import Comment


class CreateCommentCommand(AbsCommand):

    _name = "CreateCommentCommand"

    def execute(self, *args, **kwargs):
        new_comment = Comment(comment=kwargs["comment"], user=kwargs["owner"])
        COMMENTS.append(new_comment)
        new_comment.comment_id = len(COMMENTS)
        new_comment.owner.comments.append(len(COMMENTS))  # store the id of the comment
        self._message = "Comment created successfully"
        return True
