"""
Tests for the user factories
"""
from unittest import TestCase
from app.factories.admin_user_factory import AdminFactory
from app.factories.moderator_user_factory import ModeratorFactory
from app.factories.normal_user_factory import NormalUserFactory
from app.models.admin_user import AdminUser
from app.models.moderator_user import ModeratorUser
from app.models.normal_user import NormalUser


class TestAdminFactory(TestCase):

    def setUp(self):
        self._user = AdminFactory.create_user("test_user", "test_pass")

    def test_create_user(self):
        self.assertTrue(type(self._user), AdminUser)


class TestModeratorFactory(TestCase):

    def setUp(self):
        self._user = ModeratorFactory.create_user("test_user", "test_pass")

    def test_create_user(self):
        self.assertTrue(type(self._user), ModeratorUser)


class TestNormalUserFactory(TestCase):

    def setUp(self):
        self._user = NormalUserFactory.create_user("test_user", "test_pass")

    def test_create_user(self):
        self.assertTrue(type(self._user), NormalUser)
