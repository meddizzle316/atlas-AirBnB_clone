#!/usr/bin/python3
"""
Console for Airbnb clone
"""
import cmd
from models.base_model import BaseModel
import json
from models.engine.file_storage import FileStorage
from models import storage



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
        valid_classes = storage.classes()
        if buffer[0] in valid_classes.keys():
            instance = valid_classes[buffer[0]]()
            storage.new(instance)  #saves instance to filestorage dictionary
            storage.save() #converts that filestorage dictionary to json in 'file.json'
            print(f"{instance.id}")
        else:
            print("** class doesn't exist **")
        
    #prints string representation of an instance using class name and id
    def do_show(self, arg):
        """
        #prints string representation of an instance using 
        class name and id
        """
        buffer = arg.split()
        if not buffer:
            print("** class name missing **")
            return
        valid_classes = storage.classes()
        if buffer[0] in valid_classes.keys():
            storage.save()
            storage.reload()
            objects = storage.all()
            try:
                class_and_id = f"{buffer[0]}.{buffer[1]}"
            except IndexError:
                print("** instance id missing **")
                return
            if class_and_id in objects.keys():
                    print(objects[class_and_id])
            else:
                print("** no instance found **")
        else:
            print("** class doesn't exist **")
  
    
    #Deletes an instance using class and id
    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name 
        and id (save the change into the JSON file)
        """
        buffer = arg.split()
        if not buffer:
            print("** class name missing **")
            return
        valid_classes = storage.classes()
        if buffer[0] in valid_classes.keys():
            storage.reload()
            objects = storage.all()
            try:
                class_and_id = f"{buffer[0]}.{buffer[1]}"
            except IndexError:
                print("** instance id missing **")
                return
            class_and_id = f"{buffer[0]}.{buffer[1]}"
            if class_and_id in objects.keys():
                del objects[class_and_id]
                storage.save() 
            else:
                print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances 
        based or not on the class name.
        """
        buffer = arg.split()
        if not buffer:
            print("** class name missing **")
            return
        valid_classes = storage.classes()
        if buffer[0] in valid_classes.keys():
            storage.reload()
            objects = storage.all()
            list_of_objects = []
            for id in objects.keys():
                full_name = buffer[0] + "." + objects[id].__dict__['id'] 
                if full_name == id:
                    list_of_objects.append(str(objects[id]))
            if list_of_objects == []:
                    print("** instance id missing **")
                    return
            print(list_of_objects)
        else:
            print("** class doesn't exist **")


    def do_update(self, arg):
        """
         Updates an instance based on the class name 
         and id by adding or updating attribute
         (save the change into the JSON file)
        """
        buffer = arg.split()
        if not buffer:
            print("** class name missing **")
            return
        valid_classes = storage.classes()
        if buffer[0] in valid_classes.keys():
            storage.reload()
            objects = storage.all()
            try:
                class_and_id = f"{buffer[0]}.{buffer[1]}"
            except IndexError:
                print("** instance id missing **")
                return
            if class_and_id in objects.keys():
                if len(buffer) == 2:
                    print("** attribute name missing **")
                    return
                if len(buffer) == 3:
                    print("** value missing **")
                    return
                attribute_name = buffer[2]
                attribute_value = buffer[3]
                if hasattr(objects[class_and_id], attribute_name): #TODO only works when attribute already exists
                    class_attribute = getattr(objects[class_and_id], attribute_name)
                    if type(class_attribute) is str:
                        pass
                    elif type(class_attribute) is int:
                         attribute_value = int(attribute_value)
                    elif type(class_attribute) is float:
                         attribute_value = float(attribute_value)
                dict = {attribute_name:attribute_value}
                objects[class_and_id].update(**dict)
                storage.save()
            else:
                print("** no instance found **")
        else:
            print("** class doesn't exist **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
