import pathlib
import shelve
import subprocess
import os

from dictionaries import commands_decoder

def call_methods(commands:str):
    command_list = commands.split()
    if command_list[0] == commands_decoder.C_PLAY:
        music(command_list[1:])

def music(args:list):
    pass


def add(key:str, value:str):
    pass
