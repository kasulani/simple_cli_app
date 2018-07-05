from unittest import TestCase
from app.commands import load_command
from app.models.admin_user import AdminUser
from app.models.moderator_user import ModeratorUser
from app.models.normal_user import NormalUser
from app.models import COMMENTS


class TestEditCommentCommand(TestCase):
    """
    Test suite for the edit a comment command
    """

    def setUp(self):
        self._normal_user = NormalUser("test_normal_user", "test_pass")
        self._comment = "this is my comment from a normal user"
        self._create_comment = load_command("create_comment")
        self._create_comment.execute(owner=self._normal_user, comment=self._comment)
        self._edit_comment_command = load_command("edit_comment")

    def _edit_the_comment(self, user=None, new_comment=""):
        """
        This is a helper method that encapsulates the edit command
        and carries out assertions for testing purposes
        :param user:
        :return: None
        """
        self._edit_comment_command.execute(comment_id=1, new_comment=new_comment, user=user)
        self.assertEqual(self._edit_comment_command.message, "Comment edited successfully")
        self.assertNotEqual(self._comment, COMMENTS[0].comment)

    def test_admin_can_edit_a_comment(self):
        """
        This test ensures that the admin user can edit any comment
        """
        _admin = AdminUser("test_user", "test_pass")
        self._edit_the_comment(user=_admin, new_comment="this is the edited comment")

    def test_moderator_can_not_edit_a_comment(self):
        """
        This test ensures that the moderator can't edit any comment
        """
        _moderator = ModeratorUser("test_user", "test_pass")
        self.assertRaises(
            PermissionError,
            lambda: self._edit_the_comment(user=_moderator, new_comment="this is the edited comment"))
        self.assertEqual(self._edit_comment_command.message, "You don't have permission to edit a comment")

    def test_normal_user_can_edit_own_comment(self):
        """
        This test ensures that a normal user can edit their own comment
        """
        self._edit_the_comment(user=self._normal_user, new_comment="this is the edited comment")
