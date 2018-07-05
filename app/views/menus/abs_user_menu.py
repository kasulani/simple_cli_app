from abc import ABC, abstractmethod
from app.commands import load_command
from click import echo, prompt, Abort
import app.views
from app.utilities import *


class AbsUserMenu(ABC):
    """
    This an abstract base class for the comment menu each user can view
    based on there role in the system

    Notes:
        * I am using the Strategy design pattern
        * This is the interface or ABC for the strategy which has to be
        implemented by the different menu strategies, i.e normal,
        moderator and admin user
    """
    _option = None
    _options = None
    _user = None  # current logged in user

    def _execute_option(self):
        try:
            self._options[self._option]()
        except KeyError:
            self.comment_menu(error="invalid input {}".format(self._option))

    def _add_a_comment(self):
        clear_screen()
        echo("Comments > New comment")  # bread crumbs
        print_separator()
        comment = prompt("Enter your comment", type=str)
        command = load_command("create_comment")
        command.execute(comment=comment, owner=self._user)
        self.comment_menu(error=command.message)

    def _view_own_comments(self):
        command = load_command("view_own_comments")
        command.execute(owner=self._user)
        clear_screen()
        echo("Comments > Your comment(s)")  # bread crumbs
        print_separator()
        if len(command.comments) > 0:
            count = 1
            for comment in command.comments:
                echo("-> {}. {}".format(count, comment))
                count += 1
            try:
                comment_id = prompt("\nEnter an option to edit", type=int)
                self._edit_own_comments(comment=command.comments[comment_id-1])
            except Abort:
                self.comment_menu(error="")
        else:
            self.comment_menu(error=command.message)

    def _edit_own_comments(self, comment):
        clear_screen()
        echo("Comments > Your comment(s) > Edit")  # bread crumbs
        print_separator()
        echo("->" + comment)
        try:
            new_comment = prompt("\nNew comment")
        except Abort:
            self._view_own_comments()

    def _back(self):
        app.views.views.main_menu(user=self._user.username, error="")

    def _exit(self):
        app.views.views.entry_menu(user=self._user.username, error="")

    @abstractmethod
    def comment_menu(self, *args, **kwargs):
        raise NotImplementedError
