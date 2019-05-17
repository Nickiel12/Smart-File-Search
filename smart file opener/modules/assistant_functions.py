import pathlib
import shelve
import subprocess
import os

import logging
from logging import debug
logging.basicConfig(level=logging.DEBUG, format= '%(asctime)s - %(levelname)s - %(message)s')

if __name__ == "__main__":
    from dictionaries import commands_decoder
else:
    from modules.dictionaries import commands_decoder

shelf_path = pathlib.Path(str(os.path.abspath("."))) / "smart file opener" / "modules" / "assistantVariables" / "local"
debug(shelf_path)

shelf_dict = shelve.open(str(shelf_path))

def call_methods(commands:str):
    command_list = commands.split()
    if command_list[0] == commands_decoder.C_PLAY:
        if play(command_list[1:]):
            return True

def play(args:list):
    if args[1] == commands_decoder.SC_SONG:
        if song(args):
            return True

def song(args:list):
    try:
        path = shelf_dict[args[2]]
    except KeyError:
        raise ValueError("Song in assistant functions threw a key error with key : " + str(args[2]))
    process = subprocess.run(path)
    if process.returncode == 0:
        return True

def add(key:str, value:str):
    global shelf_dict
    shelf_dict[key] = value
    shelf_dict.sync()

