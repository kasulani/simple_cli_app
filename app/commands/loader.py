"""
Module to load commands
"""
from importlib import import_module
from inspect import getmembers, isabstract, isclass
from .abs_command import AbsCommand


def load_command(command):
    """
    This method loads a command
    """
    try:
        command_module = import_module('.' + command, 'app.commands')
    except ImportError:
        command_module = import_module('.no_command', 'app.commands')

    classes = getmembers(command_module,
                         lambda m: isclass(m) and not isabstract(m))

    for name, _class in classes:
        if issubclass(_class, AbsCommand):
            return _class()
