from parserregex import parser_regex

def parse(str_to_parse):
    return parser_regex.findall(str_to_parse)