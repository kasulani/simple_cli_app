from unittest import TestCase
from app.commands import load_command


class TestExitCommand(TestCase):

    def setUp(self):
        self._command = load_command("exit")

    def test_exit(self):
        self.assertRaises(
            SystemExit,
            lambda: self._command.execute())
