from collections import namedtuple
from dataclasses import dataclass
import shelve
import os
import pathlib

@dataclass
class ConstantClass():
    C_PLAY: str
    C_SHUFFLE: str
    C_dict: dict

    SC_SONG: str
    SC_dict: dict

    S_FAVORITESONG: str
    S_ALL: str
    S_dict: dict


C_PLAY = "play"
C_SHUFFLE = "shuffle"

command_dict = {
    "play": C_PLAY,
    "shuffle": C_SHUFFLE
}

SC_SONG = "music"

subcommand_dict = {
    "song": SC_SONG,
    "songs": SC_SONG,
    "music": SC_SONG,
    "tune": SC_SONG,
}

S_FAVORITESONG = "fav_song"
S_ALL = "all"

specifier_dict = {
    "favorite": S_FAVORITESONG,
    "all": S_ALL
}

commands_decoder = ConstantClass(
    C_PLAY = C_PLAY,
    C_SHUFFLE = C_SHUFFLE,
    C_dict = command_dict,
    
    SC_SONG = SC_SONG,
    SC_dict = subcommand_dict,

    S_FAVORITESONG = S_FAVORITESONG,
    S_ALL = S_ALL,
    S_dict = specifier_dict,
    )
