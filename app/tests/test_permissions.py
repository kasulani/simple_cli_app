from unittest import TestCase
from app.models.permission import Permission


class TestPermission(TestCase):

    def setUp(self):
        self.edit_perm = Permission("Edit")

    def test_get_permission(self):
        self.assertEqual(self.edit_perm.permission, "Edit")
