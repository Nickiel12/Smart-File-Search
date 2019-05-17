import pathlib
import shelve
import sys
import os

import logging
from logging import debug
logging.basicConfig(level=logging.DEBUG, format= '%(asctime)s - %(levelname)s - %(message)s')

from modules.assistant_command_functions import AssistantCommands
import stringfunctions as stringfuncs
from modules import stringparser as str_parser

shelfPath = pathlib.PurePath(os.path.abspath(".") + '/ShelfFiles/vars')
debug(shelfPath)

def read_sys_args():
    return sys.argv[1]

def get_command(input_string):
    commands = str_parser.parse(input_string)
    return commands

def openShelf():
    global shelfFile
    try:
        shelfFile = shelve.open(str(shelfPath))
        debug(shelfFile)
        return True
    except PermissionError as perm_error:
        debug("OpenShelf in 'personal_assistant threw: " + str(perm_error))
        return False

def close():
    shelfFile.close()

if __name__ == "__main__":
    if openShelf():
        args = read_sys_args()
        raw_commands = get_command(args)
        close()
    else:
        debug("Open shelf failed :(")
        quit()
