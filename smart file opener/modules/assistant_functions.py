import pathlib
import shelve
import subprocess
import os

import logging
from logging import debug
logging.basicConfig(level=logging.DEBUG,
     format= '%(asctime)s - %(levelname)s - %(message)s')

if __name__ == "__main__":
    from dictionaries import CommandConstants
else:
    from modules.dictionaries import CommandConstants

local_path = pathlib.Path("modules") / "assistantVariables" / "local"

shelf_path = pathlib.Path(str(os.path.abspath("."))) / local_path

shelf_dict = shelve.open(str(shelf_path))

def call_methods(commands:list):
    """
        Takes list of strings 'commands' and takes the first word 
        as Command, the second as Subcommand, and the third as Specifier
    """
    debug(f"call_methods called: {commands}")
    for command in commands: # Runs for loop for every string
        if type(command) != str: 
            # Checks that the current 'command' is of type str,
            # if not, it raises 'TypeError
            raise TypeError(
                f"Incorrect type passed to 'call_methods' should be 'str' but"
                + " was {type(command)}"
                )
        command_list = command.split() # split() the properly formatted str
            # The code block that executes the commands.
            # First checks if the first arg is in the dictionary
            # If it is, call the function ascribed in the dictionary,
            # passing the arguments for further excecutions 
        if command_list[0] == CommandConstants.C_PLAY: # Play
            play(command_list)
        elif command_list[0] == CommandConstants.C_ADD: # Add
            add(command_list[1], command_list[2])
        elif command_list[0] == CommandConstants.C_REMOVE:
            remove(command_list[1])

def play(args:list):
    """
        Takes args and checks the second argument against a dictionary
        and excecute the fuction returned by the dictionary
    """
    debug(f"play called: {args}")
    if type(args[1]) != str: 
            # Checks that the current keyword, args[1], is of type str,
            # if not, it raises 'TypeError
            raise TypeError(
                f"Incorrect type passed to 'call_methods' should be 'str' but"
                + " was {type(command)}"
                )
        # The code block that executes the commands.
        # First checks if the keyword, args[1],  is in the dictionary
        # If it is, call the function ascribed in the dictionary,
        # passing the arguments for further excecutions 
    if args[1] == CommandConstants.SC_SONG:
        song(args)

def song(args:list):
    """
        Takes 'args' and checks the third argument against a dictionary
        and plays the returned file path in an audio player
    """
    debug(f"song called: {args}") # logs the contents of args
        # tries to retrieve the path of the assosiated keyword in 'shelf_dict'
        # If it fails, raise a ValueError with the keyword
    try:
        path = shelf_dict[args[2]]
    except KeyError:
        raise ValueError("Song in assistant functions threw a key error with"+
        " key : " + str(args[2]))
    # Log the path returned by the dictionary search
    debug(f"song is calling: {path}")
    # Play the path with an audio player
    process = subprocess.run(['itunes', path])
    # If it runs correctly, log the path of the played audio file 
    if process.returncode == 0:
        debug(f"song was run with argument: {path}")

def add(key:str, value:str):
    """
    Adds 'key' with value 'value' to the dictionary
    """
    global shelf_dict
    shelf_dict[key] = value
    shelf_dict.sync()

def remove(key:str):
    """
    Removes 'key' from the dictionary
    """
    global shelf_dict
    del shelf_dict[key]
    shelf_dict.sync()

