"""
Tests for the commands
"""
from unittest import TestCase
from app.commands import load_command
from app.models import USERS
from app.models.admin_user import AdminUser


class TestCreateUserCommand(TestCase):
    """
    Test suite for the create a user command
    """

    def setUp(self):
        self._username = "test_user"
        self._password = "test_pass"
        self._role = "admin"
        self._command = load_command("create_user")

    def test_create_a_user_command(self):
        self._command.execute(username=self._username, password=self._password, role=self._role)
        self.assertTrue(type(USERS[0]), AdminUser)
        self.assertEqual(USERS[0].username, self._username)
        self.assertEqual(USERS[0].password, self._password)
        self.assertEqual(USERS[0].role, self._role)
