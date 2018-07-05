"""
Base class for the different user model classes
"""
from .abs_user import AbsUser


class BaseUser(AbsUser):

    def __init__(self, username="", password="", role=None):
        # todo: raise exception if username, password and role is not set at object creation
        self._username = username
        self._password = password
        self._comments = []  # stores ids of the user's comments for quick reference
        self._role = role  # todo: role has to be one of accepted types

    def __str__(self):
        return self._username

    def __repr__(self):
        return "{} - {} - {}".format(self._username, self._role.role, self._role.permissions)

    @property
    def username(self):
        """
        This method returns the username of the user
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        This method sets the username of the user
        """
        # todo: validate username
        self._username = username

    @property
    def password(self):
        """
        This method returns the password of the user
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        This method sets the password of the user
        """
        # todo: validate password
        self._password = password

    @property
    def role(self):
        """
        This method returns the role of the user as a string
        """
        return self._role.role

    @role.setter
    def role(self, role):
        """
        This method sets the role of the user
        """
        # todo: validate role
        self._role = role

    @property
    def permissions(self):
        """
        This method returns the permissions of the user
        """
        return self._role.permissions

    @property
    def comments(self):
        """
        This method returns list containing ids of comments that belong to the user
        """
        return self._comments

    @comments.setter
    def comments(self, comment_id):
        """
        This method adds a comment id to the user's comments list
        """
        # todo: validate id
        self._comments.append(comment_id)
