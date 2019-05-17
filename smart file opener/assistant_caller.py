import pathlib
import subprocess
import os

import logging
from logging import debug
logging.basicConfig(level=logging.DEBUG, format= '%(asctime)s - %(levelname)s - %(message)s')

cwd = os.path.abspath(".")
path = pathlib.PurePath(os.path.abspath("." "/personal_assistant.py"))
path = str(path)
debug(path)

def call_assistant():
    print("What is your wish master?")
    user_command = input(">>>")

    assistant_cmd = subprocess.run([path, user_command], shell=True, cwd=cwd)
    debug(assistant_cmd)

call_assistant()