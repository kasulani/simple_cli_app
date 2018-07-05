"""
    Simple CLI Application
    3-June-2018
    Emmanuel King Kasulani
"""
import click
from app.commands.loader import load_command
from app.views.views import entry_menu


@click.command()
def main():
    """
    A Simple CLI application
    """
    # create a default admin user
    load_command("create_user").execute(
        username="admin", password="admin123", role="admin")
    while True:  # main program loop
        entry_menu()


if __name__ == '__main__':
    main()
