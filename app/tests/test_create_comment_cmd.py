from unittest import TestCase
from app.commands import load_command
from app.models.admin_user import AdminUser
from app.models import COMMENTS
from app.models.comment import Comment


class TestCreateCommentCommand(TestCase):
    """
    Test suite for the create a comment command
    """

    def setUp(self):
        self._owner = AdminUser("test_user", "test_pass")
        self._comment = "this is my comment"
        self._command = load_command("create_comment")

    def test_create_a_comment_command(self):
        self._command.execute(owner=self._owner, comment=self._comment)
        self.assertTrue(type(COMMENTS[0]), Comment)
        self.assertEqual(COMMENTS[0].comment, self._comment)
        self.assertEqual(len(self._owner.comments), 1)
