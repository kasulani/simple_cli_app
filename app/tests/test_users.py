"""
Tests for models
"""
from app.models.admin_user import AdminUser
from app.models.user_role import UserRole
from app.models.admin_role import AdminRole
from app.models.moderator_role import ModeratorRole
from app.models.moderator_user import ModeratorUser
from app.models.normal_user import NormalUser
from unittest import TestCase


class BaseUserTest(TestCase):
    def setUp(self):
        self._username = "test_user"
        self._password = "test_pass"
        self._role = ""
        self._alternate_role = None  # the alternate role is used in the set role test
        self._alternate_role_str = ""  # the string representation of the alternate role

    def get_username(self):
        """
        This test ensures that a user object has a username attribute that
        can be accessed by other objects
        """
        self.assertEqual(self._user.username, self._username)

    def get_password(self):
        """
        This test ensures that a user object has a password attribute that
        can be accessed by other objects
        """
        self.assertEqual(self._user.password, self._password)

    def get_role(self):
        """
        This test ensures that a user object has a role attribute that
        can be accessed by other objects
        """
        self.assertEqual(self._user.role, self._role)

    def set_username(self):
        """
        This test ensures that we can set the username
        """
        self._user.username = "new_test_user"
        self.assertEqual(self._user.username, "new_test_user")

    def set_password(self):
        """
        This test ensures that we can set the password
        """
        self._user.password = "new_password"
        self.assertEqual(self._user.password, "new_password")

    def set_role(self):
        """
        This test ensures that we can set the role
        """
        self._user.role = self._alternate_role
        self.assertEqual(self._user.role, self._alternate_role_str)


class TestAdminUser(BaseUserTest):
    """
    Tests for the admin user
    """

    def setUp(self):
        super().setUp()
        self._role = "admin"
        self._alternate_role = UserRole()
        self._alternate_role_str = "user"
        self._user = AdminUser(self._username, self._password)

    def test_object_is_of_type_admin_user(self):
        """
        This test ensures that the user object in this test case is of the type
        AdminUser
        """
        self.assertTrue(type(self._user) is AdminUser)
        self.assertFalse(type(self._user) is ModeratorUser)
        self.assertFalse(type(self._user) is NormalUser)

    def test_get_username(self):
        self.get_username()

    def test_get_password(self):
        self.get_password()

    def test_get_role(self):
        self.get_role()

    def test_set_username(self):
        self.set_username()

    def test_set_password(self):
        self.set_password()

    def test_set_role(self):
        self.set_role()


class TestModeratorUser(BaseUserTest):
    """
    Tests for the Moderator user
    """

    def setUp(self):
        super().setUp()
        self._role = "moderator"
        self._alternate_role = AdminRole()
        self._alternate_role_str = "admin"
        self._user = ModeratorUser(self._username, self._password)

    def test_object_is_of_type_moderator_user(self):
        """
        This test ensures that the user object in this test case is of the type
        ModeratorUser
        """
        self.assertTrue(type(self._user) is ModeratorUser)
        self.assertFalse(type(self._user) is AdminUser)
        self.assertFalse(type(self._user) is NormalUser)

    def test_get_role(self):
        self.get_role()

    def test_set_role(self):
        self.set_role()


class TestNormalUser(BaseUserTest):
    """
    Tests for the Normal user
    """

    def setUp(self):
        super().setUp()
        self._role = "user"
        self._alternate_role = ModeratorRole()
        self._alternate_role_str = "moderator"
        self._user = NormalUser(self._username, self._password)

    def test_object_is_of_type_moderator_user(self):
        """
        This test ensures that the user object in this test case is of the type
        NormalUser
        """
        self.assertTrue(type(self._user) is NormalUser)
        self.assertFalse(type(self._user) is AdminUser)
        self.assertFalse(type(self._user) is ModeratorUser)

    def test_get_role(self):
        self.get_role()

    def test_set_role(self):
        self.set_role()
