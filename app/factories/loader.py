"""
Module to load factories
"""
from importlib import import_module
from inspect import getmembers, isabstract, isclass
from .abs_user_factory import AbsUserFactory


def load_user_factory(factory):
    """
    This method loads a user factory
    """
    try:
        command_module = import_module('.' + factory, 'app.factories')
    except ImportError:
        command_module = import_module('.null_user_factory', 'app.factories')

    classes = getmembers(command_module,
                         lambda m: isclass(m) and not isabstract(m))

    for name, _class in classes:
        if issubclass(_class, AbsUserFactory):
            return _class
