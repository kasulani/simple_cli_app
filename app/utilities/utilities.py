"""
This module has a collection of helper functions
"""
from click import echo, clear, style
from app.models import USERS


def print_banner():
    """
    This is helper function prints out an application banner
    """
    echo("Simple CLI APP 1.0.0")


def print_separator():
    """
    This is helper function prints out a separator
    """
    echo("---------------------------------")


def print_error(error=""):
    """
    This is a helper function to print out errors messages on the screen
    """
    if error:
        print_separator()
        echo(style("-> " + error, fg='red'))
        print_separator()


def clear_screen():
    """
    This is a helper function to clear the screen
    """
    clear()
    print_banner()
    print_separator()


def fetch_user(username=""):
    """
    This helper function finds and returns a user object given a username
    :param username:
    :return user:
    """
    for user in USERS:
        if user.username == username:
            return user
    return None
