from collections import namedtuple
from dataclasses import dataclass
import shelve
import os
import pathlib

all_constants = (
    "C_PLAY"
    "C_SHUFFLE"
    "C_dict"

    "SC_SONG"
    "SC_dict"

    "S_FAVORITESONG"
    "S_dict"

)

@dataclass
class ConstantClass():
    C_PLAY: str
    C_SHUFFLE: str
    C_dict: dict

    SC_SONG: str
    SC_dict: dict

    S_FAVORITESONG: str
    S_dict: dict


C_PLAY = "play"
C_SHUFFLE = "shuffle"

command_dict = {
    "play": C_PLAY,
}

SC_SONG = "music"

subcommand_dict = {
    "song": SC_SONG,
    "music": SC_SONG,
    "tune": SC_SONG,
}

S_FAVORITESONG = "fav_song"

specifier_dict = {
    "favorite": S_FAVORITESONG,
}

commands_decoder = ConstantClass(
    C_PLAY = C_PLAY,
    C_SHUFFLE = C_SHUFFLE,
    C_dict = command_dict,
    
    SC_SONG = SC_SONG,
    SC_dict = subcommand_dict,

    S_FAVORITESONG = S_FAVORITESONG,
    S_dict = specifier_dict,
    )

def build_shelf():
    path = pathlib.PurePath(os.path.abspath(".") + "/smart file opener/modules/dict_shelf/dictShelf")
    print(path)
    shelf = shelve.open(str(path))
    shelf["command_consts"] = commands_decoder
    shelf.close()

build_shelf()