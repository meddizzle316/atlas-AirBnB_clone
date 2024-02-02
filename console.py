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

    def emptyline(self):
        """
        Called when empty line is passed
        Useed to override command to keep from repeating previous command
        """
        pass

    def default(self, line: str):
        self.line = line.strip()

    def input_checker(self, buffer):
        """
        Checks to see if input is empty or valid

        Args:
            buffer (str): User input if there is any

        Returns:
            _type_: _description_
        """
        if self.line:
            print(self.line)
        else:
            pass

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
