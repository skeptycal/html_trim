#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
""" html_trim.py """
# @imports
import json  # requires python >= 2.6
import sys
from typing import Dict

# @info
name = "lnbin"
json_file = sys.path[0] + "/" + name + ".json"

# @functions


def get_json(file: str = json_file) -> Dict:
    """ Get program info from json file. """
    with open(file, "r") as read_file:
        data = json.load(read_file)
    return data


def put_json(data: Dict, file: str = json_file) -> int:
    """ Write program info to json file. """
    with open(file, "w") as write_file:
        json.dump(data, write_file)


def create_usage(data: Dict) -> str:
    """ Create program usage info from json file. """
    usage = data["name"]
    return usage


def create_version(data: Dict) -> str:
    """ Create program version info from json file. """
    usage = data
    print(data)
    return usage


# @mainloop


def mainloop() -> int:
    """ Main Loop """
    json_data = get_json(json_file)
    version = create_version(json_data)
    print(version)
    return 0


# @cli_main
if __name__ == "__main__":
    print("Here: ", json_file)
    mainloop()
