from parserregex import parser_regex
import shelve

def parse(str_to_parse):
    raw_command_list = str_to_parse.split()
    command_list = decode(raw_command_list)

def decode(raw_list):
    command_list = []
    subcommand_list = []
    specifier_list = []

    for i in raw_list:
        try:
            command_list.append(commands_decoder.C_dict[i])
        except KeyError:
            try:
                subcommand_list.append(commands_decoder.SC_dict[i])
            except KeyError:
                try:
                    specifier_list.append(commands_decoder.S_dict[i])
                except KeyError:
                    continue

if __name__ == "__main__":
    print(parse("play my favorite song"))