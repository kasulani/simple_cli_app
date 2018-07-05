from unittest import TestCase
from app.commands import load_command
from app.models.normal_user import NormalUser


class TestViewOwnCommentsCommand(TestCase):
    """
    Test suite for the view own comments command
    """

    def setUp(self):
        self._owner = NormalUser("test_user", "test_pass")
        self._comment = "this is my comment"
        self._create_comment_cmd = load_command("create_comment")
        self._create_comment_cmd.execute(owner=self._owner, comment=self._comment)
        self._command = load_command("view_own_comments")

    def test_view_own_comments_command(self):
        self._command.execute(owner=self._owner)
        self.assertTrue(type(self._command.comments), str)
        self.assertEqual(self._command.comments[0], self._comment)
        self.assertEqual(len(self._command.comments), 1)
