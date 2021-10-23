#!/usr/bin/env python3
"""
Script to solve day 8 of the 2020 Advent of Code.

https://adventofcode.com/2020/day/8
"""

import re
import logging

################################################################################

log = logging.getLogger(__name__)

COMMAND_RE = r"^(?P<cmd>[a-zA-Z]{3}) (?P<op>[-+])(?P<num>\d*)$"

################################################################################

class Command:
    """Class to represent commands."""

    __commands = set()

    ########################################

    def __init__(self, name: str, op: str, num: int):
        self.name = name
        self.op = op
        self.num = num

    ########################################

    def handle_cmd(self, ctx):
        log.warning(f"Command {self.name} handled by base class (noop).")
        pass

    ########################################

    @classmethod
    def handles(cls, name: str):
        """Return true if this class handles a command with 'name'."""
        return False

    ########################################

    @classmethod
    def register_command(cls, command):
        """Register a class prototype."""
        if issubclass(command, cls) and command is not cls:
            cls.__commands.add(command)
        else:
            log.error("Cannot register command")

    ########################################

    def __new__(cls, name: str, *args, **kwargs):
        """Instantiate a command instance"""
        for command in cls.__commands:
            if command.handles(name):
                return object.__new__(command)

        raise RuntimeError(f"No class to handle command {name}", name)

################################################################################

class nopCommand(Command):
    """Handles the 'nop' command"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    ########################################

    def handle_cmd(self, ctx):
        log.info(f"Command {self.name} is a null operation.")

    ########################################

    @classmethod
    def handles(cls, name: str):
        """Return true if this class handles a command with 'name'."""
        if name == "nop":
            return True

        return False

################################################################################

class jmpCommand(Command):
    """Handles the 'jmp' command"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    ########################################

    def handle_cmd(self, ctx):
        log.info(f"Command {self.name} is a jump operation.")

    ########################################

    @classmethod
    def handles(cls, name: str):
        """Return true if this class handles a command with 'name'."""
        if name == "jmp":
            return True

        return False

################################################################################

class accCommand(Command):
    """Handles the 'acc' command"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    ########################################

    def handle_cmd(self, ctx):
        log.info(f"Command {self.name} is a acc operation.")

    ########################################

    @classmethod
    def handles(cls, name: str):
        """Return true if this class handles a command with 'name'."""
        if name == "acc":
            return True

        return False

################################################################################

# Register the command prototypes.
Command.register_command(nopCommand)
Command.register_command(jmpCommand)
Command.register_command(accCommand)