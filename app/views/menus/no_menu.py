from click import echo, prompt
from .abs_user_menu import AbsUserMenu
from app.utilities import *


class NoMenu(AbsUserMenu):

    def __init__(self, user):
        self._user = user
        self._options = {
            1: self._back
        }

    def comment_menu(self, **kwargs):
        clear_screen()
        echo("Choose an option:\n\t1. Back")
        print_error(error=kwargs.get("error", ""))
        self._option = prompt("Enter an option", type=int)
        self._execute_option()
