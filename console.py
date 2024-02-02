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

    prompt = "(hbnb) "


    # Exit command
    def do_EOF(self, arg):
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
