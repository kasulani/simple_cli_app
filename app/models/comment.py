"""
Comment model
"""


class Comment:

    def __init__(self, comment_id=0, comment="", user=None):
        self._comment_id = comment_id
        self._comment = comment
        self._owner = user

    def __str__(self):
        return self._comment

    def __repr__(self):
        return "{} - {} - {}".format(self._comment_id, self._comment, self._owner)

    @property
    def comment_id(self):
        return self._comment_id

    @comment_id.setter
    def comment_id(self, _id):
        self._comment_id = _id

    @property
    def owner(self):
        return self._owner

    @property
    def comment(self):
        return self._comment

    @comment.setter
    def comment(self, comment):
        self._comment = comment
