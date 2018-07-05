from click import echo, prompt
from .abs_user_menu import AbsUserMenu
from app.utilities import *


class NormalUserMenu(AbsUserMenu):

    def __init__(self, user):
        self._user = user
        self._options = {
            1: self._add_a_comment,
            2: self._view_own_comments,
            3: self._back,
            4: self._exit
        }

    def comment_menu(self, *args, **kwargs):
        clear_screen()
        echo("Comments")
        print_separator()
        echo("Choose an option:\n\t1. New comment\n\t2. My comments\n\t3. Back\n\t4. Logout")
        print_error(error=kwargs.get("error", ""))
        self._option = prompt("Enter an option", type=int)
        self._execute_option()
