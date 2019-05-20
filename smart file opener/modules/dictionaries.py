from collections import namedtuple
from dataclasses import dataclass
import shelve
import os
import pathlib

@dataclass
class CommandConstants():

    C_ADD = "add"
    C_PLAY = "play"
    C_REMOVE = "remove"
    C_SHUFFLE = "shuffle"
    

    C_DICT = {
        "add": C_ADD,
        "play": C_PLAY,
        "remove": C_REMOVE,
        "shuffle": C_SHUFFLE,
    }

    SC_SONG = "music"

    sc_DICT = {
        "song": SC_SONG,
        "songs": SC_SONG,
        "music": SC_SONG,
        "tune": SC_SONG,
    }

    S_FAVORITESONG = "fav_song"
    S_ALL = "all"

    S_DICT = {
        "favorite": S_FAVORITESONG,
        "all": S_ALL,
    }
