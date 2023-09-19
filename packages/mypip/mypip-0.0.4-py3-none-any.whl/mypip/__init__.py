#!/usr/bin/env python3
import os
import sys

import codefast as cf
import requests

from .config import PIP_URL


def check_url_file_exist(url):
    response = requests.head(url)
    return response.status_code == requests.codes.ok


def install_private(module_name: str) -> bool:
    url = cf.b64decode(PIP_URL).rstrip()
    url = f'{url}/{module_name}.tgz'
    if check_url_file_exist(url):
        os.system(f'pip install {url}')
        return True
    else:
        cf.info(f'No private module {module_name} found in {url}')
    return False


def install_public(module_name: str):
    os.system(f'pip install {module_name}')


def pip_install():
    module_name = sys.argv[1]
    b = install_private(module_name)
    if not b:
        return install_public(module_name)
