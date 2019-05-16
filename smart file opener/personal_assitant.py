import shelve
import pathlib
import os

import logging
from logging import debug
logging.basicConfig(level=logging.DEBUG, format= '%(asctime)s - %(levelname)s - %(message)s')

import stringfunctions as stringfuncs

from modules import stringparser as str_parser

shelfPath = pathlib.PurePath(os.path.abspath(".") + '/ShelfFiles/vars')
debug(shelfPath)

def get_command(input_string):
    commands = str_parser.parse(input_string)

def openShelf():
    global shelfFile
    shelfFile = shelve.open(str(shelfPath))
    debug(shelfFile)

def testfirst():
    shelfFile["hello"] = "this is not a test"
    debug(shelfFile["hello"])

def testsecond():
    debug(shelfFile["hello"])

def store(key, value):
    key = stringfuncs.prepare_string(key)
    shelfFile[key] = value
    debug(shelfFile[key])

def read(key):
    value = shelfFile[key]
    return value

def close():
    shelfFile.close()

if __name__ == "__main__":
    openShelf()
    testsecond()
    close()
