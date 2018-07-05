from .abs_permission import AbsPermission


class Permission(AbsPermission):
    """
    Permissions class
    """

    def __init__(self, perm=""):
        self._perm = perm

    @property
    def permission(self):
        return self._perm

    def __str__(self):
        return self._perm

    def __repr__(self):
        return self._perm


class NullPermission(Permission):
    """
    Null Permissions class
    """

    def __init__(self):
        self._perm = None
