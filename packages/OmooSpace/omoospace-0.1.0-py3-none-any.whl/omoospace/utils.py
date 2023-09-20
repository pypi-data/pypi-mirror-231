import re
import os
from pathlib import Path

import yaml


def convert_to_pascalcase(string, debug=False):
    from pypinyin import lazy_pinyin
    if (debug):
        print('Original: ', string)

    # pinyin
    string = " ".join(lazy_pinyin(string))

    # [A-Za-z0-9_] only
    string = re.sub(r'[^\w]', ' ', string)
    if (debug):
        print('[A-Za-z0-9_] only: ', string)

    # Split by space
    parts = string.replace("_", " ").split()
    if (debug):
        print('All Parts: ', parts)

    # to PascalCase
    parts = [part.title() if part.islower() else part for part in parts]
    string = ''.join(parts)
    if (debug):
        print('All Parts to PascalCase: ', parts)

    return string


def receding_path(path):
    parts = Path(path).parts
    for n in range(len(parts), 1, -1):
        yield os.path.join(*parts[:n])


def detect_omoospace_yml(detect_path='.', allow_fail=True):
    detect_path = os.path.abspath(detect_path)
    space_info = None
    space_root = None
    for dir in receding_path(detect_path):
        space_yml_path = os.path.join(dir, 'OmooSpace.yml')
        if (os.path.isfile(space_yml_path)):
            with open(space_yml_path, 'r') as file:
                space_info = yaml.safe_load(file)
                space_root = dir
            break
    if not space_info:
        print('No OmooSpace detected...')
        if not allow_fail:
            raise ('No OmooSpace detected...')

    return space_root, space_info
