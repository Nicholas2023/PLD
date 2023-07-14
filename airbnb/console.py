#!/usr/bin/python3
"""
Command interpreter for the HBNB project
"""
import cmd
import re
from shlex import split

import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


# A global constant since both functions within and outside uses it
cls = [
    "BaseModel"
    "User"
    "State"
    "City"
    "Amenity"
    "Place"
    "Review"
]


def parse(arg):
    """
    Tokenize args
    """
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl


def check_args(args):
    """
    Check if arguments are valid
    Args:
        args (str): Command interface arguments
    Returns:
        (str): Error messages if args is None or not valid
    """
    arg_list = parse(args)

    if len(arg_list) == 0:
        print("** class name missing **")
    elif arg_list[0] not in cls:
        print("** class doesn't exist **")
    else:
        return arg_list


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter class for the HBNB project
    Attributes:
        prompt (str): The prompt displayed in the command line interface
    """
    prompt = "(hbnb) "
    storage = models.storage

    def default(self, arg):
        """
        Default behaviour for cmd module when input is invalid
        """
        action_map = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update,
            "create": self.do_create
        }

        match = re.search(r"\.", arg)
        if match:
            arg1 = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", arg1[1])
            if match:
                command = [arg1[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in action_map:
                    call = "{} {}".format(arg1[0], command[1])
                    return action_map[command[0]](call)

        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_quit(self, arg):
        """
        Quit command to exit the program
        Usage: quit
        """
        return True

    def do_EOF(self, arg):
        """
        Exit the command interpreter using EOF (Ctrl+D)
        """
        print()  # Print a new line before exiting
        return True

    def emptyline(self):
        """
        Do nothing when an empty line is entered
        """
        pass

    def do_create(self, argv):
        """
        Create a new instance of BaseModel, save it to the JSON file,
        and print the id
        Usage:
            Create <class_name> [<param_name>=<param_value>...]
        """
        args = check_args(argv)
        if args:
            print(eval(args[0])().id)
            self.storage.save()

    def do_show(self, argv):
        """
        Prints the string representation of an instance based on the
        class name and id
        """
        args = check_args(argv)
        if args:
            if len(args) != 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(args[0], args[1])
                if key not in self.storage.all():
                    print("** no instance found **")
                else:
                    print(self.storage.all()[key])

    def do_destroy(self, argv):
        """
        Deletes an instance based on the class name and id
        """
        args = check_args(argv)
        if args:
            if len(args) == 1:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(*args)
                if key in self.storage.all():
                    del self.storage.all()[key]
                    self.storage.save()
                else:
                    print("** no instance found **")

    def do_all(self, argv):
        """
        Prints all instances based on the class name
        """
        args = split(argv)
        objects = self.storage.all().values()
        if not args:
            print([str(obj) for obj in objects])
        else:
            if args[0] not in cls:
                print("** class doesn't exist **")
            else:
                print([str(obj) for obj in objects
                       if args[0] in str(obj)])

    def do_update(self, argv):
        """
        Updates an instance based on the class name and id by
        adding or updating attributes
        """
        arg_list = check_args(argv)
        if arg_list:
            if len(arg_list) == 1:
                print("** instance id missing **")
            else:
                instance_id = "{}.{}".format(arg_list[0], arg_list[1])
                if instance_id in self.storage.all():
                    if len(arg_list) == 2:
                        print("** attribute name missing **")
                    elif len(arg_list) == 3:
                        print("** value missing **")
                    else:
                        obj = self.storage.all()[instance_id]
                        if arg_list[2] in type(obj).__dict__:
                            v_type = type(obj.__class__.__dict__[arg_list[2]])
                            setattr(obj, arg_list[2], v_type(arg_list[3]))
                        else:
                            setattr(obj, arg_list[2], arg_list[3])
                else:
                    print("** no instance found **")

            self.storage.save()

    def do_count(self, arg):
        """
        Retrieve the number of instances of a class
        """
        arg1 = parse(arg)
        count = 0
        for obj in models.storage.all().values():
            if arg1[0] == type(obj).__name__:
                count += 1
        print(count)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
