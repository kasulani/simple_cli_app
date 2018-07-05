# Simple CLI
## About
This is a simple CLI program that allows users to create comments. Users come in 3 roles: normal users, moderators, and 
admins. Normal users can only create new comments, and edit the their own comments. Moderators have the added ability 
to delete comments (to remove trolls), while admins have the ability to edit or delete any comment.

The full description of the coding challenge can be found in the directory named challenge.
## Goal
The goal of this project is enable me explore and learn the features of the [click](http://click.pocoo.org/5/) library.
## Features
With this simple CLI application;
- users can log in and out
- users can add a comment
- users can edit a comment
- users can reply to a comment
## Requirements
- Python 3.x.x+
- Click
- Pytest
## Tests
"Code without tests is broken as designed", said  [Jacob Kaplan-Moss](https://jacobian.org/writing/django-apps-with-buildout/#s-create-a-test-wrapper). Therefore i shall not give you code that
can not be tested or has no tests. So, to run tests, enter the following command
```sh 
    $ python -m unittest tests/tests
```
## Running the application
To run this application, clone the repository on your local machine and execute the following command.
```sh
    $ cd simple_cli
    $ virtualenv virtenv
    $ source virtenv/bin/activate
    $ pip install -r requirements.txt
    $ nohup python run.py & disown
```