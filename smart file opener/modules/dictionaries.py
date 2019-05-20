from collections import namedtuple
from dataclasses import dataclass
import shelve
import os
import pathlib

@dataclass
class ConstantClass():

    C_ADD = "add"
    C_PLAY = "play"
    C_SHUFFLE = "shuffle"

    C_DICT = {
        "play": C_PLAY,
        "shuffle": C_SHUFFLE,
        "add": C_ADD,
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
