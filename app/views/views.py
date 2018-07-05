"""
Views for the simple CLI application

Notes:
    * I am using the Command design pattern.
    * The view functions are the invokers.
    * View functions don't manipulate model object as that would be a violation of
    the single responsibility principle in S.O.L.I.D. Their only function is to
    print messages and menus to the user to interact with.
"""
from click import echo, prompt
from app.commands.loader import load_command
from app.utilities import *
from .menus import load_menu


def entry_menu(**kwargs):
    """
    This view method prints an entry menu which is the first menu in the life cycle
    of the application
    """
    options = {
        1: create_a_user,
        2: login_a_user,
        3: load_command("exit")
    }
    clear_screen()
    echo("Choose an option:\n\t1. Register\n\t2. Login\n\t3. Exit")
    print_error(error=kwargs.get("error", ""))
    option = prompt("Enter an option", type=int)
    try:
        if option == 3:
            options[option].execute()
        options[option]()
    except KeyError:
        entry_menu(error="invalid input {}".format(option))


def main_menu(**kwargs):
    """
    This is the application main menu. This menu is viewed by a user who is logged in
    """
    options = {
        1: comments_menu,
        2: entry_menu
    }
    clear_screen()
    echo("Welcome {}\n".format(kwargs.get("user", "anonymous")))
    echo("Choose an option:\n\t1. Comment\n\t2. Logout")
    print_error(error=kwargs.get("error", ""))
    option = prompt("Enter an option", type=int)
    try:
        options[option](user=kwargs.get("user", None))
    except KeyError:
        main_menu(
            user=kwargs.get("user", "anonymous"),
            error="invalid input {}".format(option)
        )


def comments_menu(**kwargs):
    """
    This view function provides an interface for a user to create, view, edit, delete
    comments.

    Notes:
        * I am using the strategy design pattern so select which menu to load
        * This view method is the context
    """
    user = fetch_user(username=kwargs.get("user", "anonymous"))
    menu = load_menu(user=user)  # load a menu based on the user's role
    menu.comment_menu(error=kwargs.get("error", ""))


def create_a_user():
    """
    This view methods provides an interface for creating a new user
    """
    clear_screen()
    echo("Register a new user account")
    print_separator()
    username = prompt("> Enter your username")
    password = prompt("> Enter your password", hide_input=True)
    confirm_password = prompt("> Confirm your password", hide_input=True)
    # todo: check password length and strength
    # todo: check username length and validity
    if password != confirm_password:
        msg = "Invalid password."
    else:
        command = load_command("create_user")
        command.execute(
            username=username, password=password, role="normal")
        msg = command.message

    entry_menu(error=msg)  # todo: change the key from error to info


def login_a_user():
    """
    This view methods provides an interface for logging in a user
    """
    clear_screen()
    echo("User login")
    print_separator()
    username = prompt("> username")
    password = prompt("> password", hide_input=True)
    command = load_command("login")
    try:
        command.execute(username=username, password=password)
        main_menu(user=username, error=command.message)
    except PermissionError:
        entry_menu(error=command.message)
