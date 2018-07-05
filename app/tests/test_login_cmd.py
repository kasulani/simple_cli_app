from unittest import TestCase
from app.commands import load_command


class TestLoginCommand(TestCase):

    def setUp(self):
        self._username = "test_user"
        self._password = "test_pass"
        self._login_cmd = load_command("login")
        self._create_user_cmd = load_command("create_user")
        self._create_user_cmd.execute(
            username=self._username,
            password=self._password, role="admin")

    def test_login_existing_user(self):
        """
        This test ensures that an existing user can login successfully
        """
        self._login_cmd.execute(username=self._username, password=self._password)
        self.assertEqual(self._login_cmd.message, "User login was successful")

    def test_login_non_existing_user(self):
        """
        This test ensures that a non existing user can't login successfully
        """
        self.assertRaises(
            PermissionError,
            lambda: self._login_cmd.execute(username="fake_user", password="fake_pass"))
        self.assertEqual(self._login_cmd.message, "User login failed")
