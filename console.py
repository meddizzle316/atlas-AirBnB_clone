#!/usr/bin/python3
"""
Console for Airbnb clone
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    Attributes and methods for Airbnb console
    """

    # Exit command
    def do_exit(self, arg):
        """
        Exits console interface

        Returns:
            True
        """
        print("Have a pleasant day")
        return True

    # Quit command
    def do_quit(self, arg):
        """
        Quits console interface

        Returns:
            True
        """
        print("Have a pleasant day")
        return True
