#!/usr/bin/python3
"""
Console for Airbnb clone
"""
import cmd
from models.base_model import BaseModel



class HBNBCommand(cmd.Cmd):
    """
    Attributes and methods for Airbnb console
    """

    prompt = "(hbnb)"
    intro = "Type help or ? to list commands"


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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
