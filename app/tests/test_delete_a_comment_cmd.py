from unittest import TestCase
from app.commands import load_command
from app.models.admin_user import AdminUser
from app.models.moderator_user import ModeratorUser
from app.models.normal_user import NormalUser
from app.models import COMMENTS


class TestDeleteCommentCommand(TestCase):
    """
    Test suite for the delete a comment command
    """

    def setUp(self):
        self._normal_user = NormalUser("test_normal_user", "test_pass")
        self._comment = "this is my comment from a normal user"
        self._create_comment = load_command("create_comment")
        self._create_comment.execute(owner=self._normal_user, comment=self._comment)
        self._delete_comment_command = load_command("delete_comment")

    def _delete_the_comment(self, user=None):
        """
        This is a helper method that encapsulates the delete command
        and carries out assertions for testing purposes
        :param user:
        :return: None
        """
        self.assertEqual(len(COMMENTS), 1)
        self._delete_comment_command.execute(comment_id=1, user=user)
        self.assertEqual(self._delete_comment_command.message, "Comment deleted successfully")
        self.assertEqual(len(COMMENTS), 0)

    def test_admin_can_delete_a_comment(self):
        """
        This test ensures that the admin user can delete any comment
        """
        _admin = AdminUser("test_user", "test_pass")  # admin can delete a comment
        self._delete_the_comment(user=_admin)
        # this assertion below ensures the comment id no longer part of the owners comments
        self.assertTrue(1 not in self._normal_user.comments)

    def test_moderator_can_delete_a_comment(self):
        """
        This test ensures that the moderator can delete any comment
        """
        _moderator = ModeratorUser("test_user", "test_pass")  # moderator can delete a comment
        self._delete_the_comment(user=_moderator)
        # this assertion below ensures the comment id no longer part of the owners comments
        self.assertTrue(1 not in self._normal_user.comments)

    def test_normal_user_can_not_delete_a_comment(self):
        """
        This test ensures that a normal user can't delete any comment, even the ones they
        have created
        """
        self.assertRaises(PermissionError, lambda: self._delete_the_comment(user=self._normal_user))
        self.assertEqual(self._delete_comment_command.message, "You don't have permission to delete a comment")
