"""
Tests for the comment model
"""
from unittest import TestCase
from app.models.normal_user import NormalUser
from app.models.comment import Comment


class TestComments(TestCase):

    def setUp(self):
        self._user = NormalUser("test_user", "test_pass")
        self._comment_str = "this is a test comment"
        self._comment = Comment(1, self._comment_str, self._user)

    def test_comment_owner(self):
        """
        This test ensures that the owner of the comment is the one who created
        it
        """
        self.assertEqual(self._comment.owner, self._user)

    def test_get_comment(self):
        """
        This test ensures that the comment can be accessed by other objects in the
        system
        """
        self.assertEqual(self._comment.comment, self._comment_str)

    def test_set_comment(self):
        """
        This test ensures that the comment can be set by other objects in the system
        """
        new_comment = "This is another comment"
        self._comment.comment = new_comment
        self.assertEqual(self._comment.comment, new_comment)
