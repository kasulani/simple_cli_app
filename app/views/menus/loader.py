"""
Module to load appropriate user menu
"""
from importlib import import_module
from inspect import getmembers, isabstract, isclass
from .abs_user_menu import AbsUserMenu


def load_menu(user):
    """
    This method loads a menu
    """
    menu = user.role + "_user_menu"
    try:
        command_module = import_module('.' + menu, 'app.views.menus')
    except ImportError:
        command_module = import_module('.no_menu', 'app.views.menus')

    classes = getmembers(command_module,
                         lambda m: isclass(m) and not isabstract(m))

    for name, _class in classes:
        if issubclass(_class, AbsUserMenu):
            return _class(user=user)
