"""
Base class for the role
"""
from .abs_role import AbsRole


class BaseRole(AbsRole):

    def __init__(self, role):
        self._role = role
        self._permissions = None

    @property
    def role(self):
        return self._role

    @property
    def permissions(self):
        """
        This method returns permissions as a list of strings.
        """
        permissions = []
        for perm in self._permissions:
            permissions.append(perm.permission)
        return permissions

    def __str__(self):
        return self._role

    def __repr__(self):
        return "{} - {}".format(self._role, self._permissions)
