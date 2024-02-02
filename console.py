#!/usr/bin/python3
"""
Console for Airbnb clone
"""
import cmd
from models.base_model import BaseModel
import json



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
            return self.line
        else:
            pass

    # Exit command
    def do_EOF(self, arg):
        """
        Command that exits console interface

        Returns:
            True
        """
        print("Have a pleasant day")
        return True

    # Quit command
    def do_quit(self, arg):
        """
        Command that quits console interface

        Returns:
            True
        """
        print("Have a pleasant day")
        return True

    # Create command
    def do_create(self, arg):
        """
        Command that creates a new instance of the class

        Returns:
            A new instance of the class and saves it to a JSON
        """
        buffer = arg.split()
        if not buffer:
            print("** class name missing **")
            return
        buffer = buffer[0]
        if buffer == "BaseModel":
            instance = BaseModel()
            instance.to_dict()
            print(f"{instance.id}")
        else:
            print("** class doesn't exsist **")
        

if __name__ == '__main__':
    HBNBCommand().cmdloop()
