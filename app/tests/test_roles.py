"""
Test roles
"""
from unittest import TestCase
from app.models.admin_role import AdminRole
from app.models.moderator_role import ModeratorRole
from app.models.user_role import UserRole


class BaseRoleTest(TestCase):

    def setUp(self):
        self._role = None
        self._role_str = ""
        self._edit = "edit"
        self._delete = "delete"

    def get_role(self):
        """
        This test ensures that the role created is set.
        """
        self.assertEqual(self._role.role, self._role_str)

    def get_permissions(self):
        """
        This test ensures that the role created has the expected permissions set. Over ride
        this method in the specific test case for a role.
        """
        pass


class TestAdminRole(BaseRoleTest):

    def setUp(self):
        super().setUp()
        self._role = AdminRole()
        self._role_str = "admin"

    def get_permissions(self):
        self.assertIn(self._edit, self._role.permissions)
        self.assertIn(self._delete, self._role.permissions)

    def test_get_role(self):
        self.get_role()

    def test_get_permissions(self):
        """
        This test ensures that the admin role has the permission to edit and delete
        other user comments
        """
        self.get_permissions()


class TestModeratorRole(BaseRoleTest):

    def setUp(self):
        super().setUp()
        self._role = ModeratorRole()
        self._role_str = "moderator"

    def get_permissions(self):
        self.assertNotIn(self._edit, self._role.permissions)
        self.assertIn(self._delete, self._role.permissions)

    def test_get_role(self):
        self.get_role()

    def test_get_permissions(self):
        """
        This test ensures that the moderator role has permission to edit other
        user comments but does not have permission to delete them
        """
        self.get_permissions()


class TestUserRole(BaseRoleTest):

    def setUp(self):
        super().setUp()
        self._role = UserRole()
        self._role_str = "normal"

    def test_get_role(self):
        self.get_role()

    def test_get_permissions(self):
        """
        This test ensures that the user role has no permissions over other users'
        comments
        """
        self.assertEqual(len(self._role.permissions), 0)
        self.assertNotIn(self._edit, self._role.permissions)
        self.assertNotIn(self._delete, self._role.permissions)
