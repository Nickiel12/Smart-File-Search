
import logging
from logging import debug
logging.basicConfig(level=logging.DEBUG, format= '%(asctime)s - %(levelname)s - %(message)s')

if __name__ == "__main__":
    from dictionaries import CommandConstants
else:
    from modules.dictionaries import CommandConstants

local_path = pathlib.Path("modules") / "assistantVariables" / "local"

shelf_path = pathlib.Path(str(os.path.abspath("."))) / local_path

shelf_dict = shelve.open(str(shelf_path))

def parse(str_to_parse):
    raw_command_list = str_to_parse.split()

    decoded_command_list = decode(raw_command_list)
    debug("decoded commands: " + str(decoded_command_list))

    commands = build_commands(decoded_command_list)
    debug("built commands: " + str(commands))
    return commands

def decode(raw_list):
    command_list = []
    subcommand_list = []
    specifier_list = []

    for i in raw_list:
        try:
            command_list.append(CommandConstants.C_dict[i])
            if command_list[0] == CommandConstants.C_PLAY:
                if special_case(command_list[0], raw_list):
                    break
        except KeyError:
            try:
                subcommand_list.append(CommandConstants.SC_dict[i])
            except KeyError:
                try:
                    specifier_list.append(CommandConstants.S_dict[i])
                except KeyError:
                    continue
    return [command_list, subcommand_list, specifier_list]

def build_commands(parsed_command_list):
    command_list, subcommand_list, specifier_list = parsed_command_list
    built_commands = []

    for i in range(0, len(command_list)):
        current_list = [
            command_list[i],
            subcommand_list[i],
            specifier_list[i]
        ]

        current_command = " ".join(current_list)
        built_commands.append(current_command)
    return built_commands

def special_case(case, commands) -> bool:
    if case == CommandConstants.C_PLAY:
        for i in range(len(commands[1:])):
            try:
                shelf_dict[str(commands)]
        return True

if __name__ == "__main__":
    print(parse("shuffle all songs"))
    """
        list of possible test phrases:
            make {songName} my favorite song #NIY!!!!!!
            play my favorite song
            play all songs
            shuffle all songs
            #shuffle all with my favorite song first #not sure if multiple requests are going to be available
    """