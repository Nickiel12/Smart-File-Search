import pathlib
import subprocess
import os

import logging
from logging import debug
logging.basicConfig(level=logging.DEBUG, format= '%(asctime)s - %(levelname)s - %(message)s')

cwd = os.path.abspath(".")
path = pathlib.Path(str(cwd)) / "personal_assistant.py"
path = str(path)
debug(path)

def call_assistant():
    print("What is your wish master?")
    user_command = input(">>>")

    if user_command == "gui":
        gui_cwd = pathlib.Path(cwd) / 'guis'
        gui_path = pathlib.Path(str(cwd)) / "guis" / "gui_run.bat"
        gui_path = str(gui_path)
        assistant_cmd = subprocess.run([gui_path], shell=True, cwd = gui_cwd)
    else:
        assistant_cmd = subprocess.run([path, user_command], shell=True, cwd=cwd)
    debug(assistant_cmd)

call_assistant()