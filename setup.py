from setuptools import find_packages, setup
from typing import List

NAME = "sensor fault detection"
VERSION = "0.0.1"
AUTHER = "sunand"
AUTHER_EMAIL_ID = "sunandd92@gmail.com"
REQUIRMENTS_FILE_NAME = "requirements.txt"
HYPEN_E_DOT = "-e ."

def get_requirments(file_path:str = REQUIRMENTS_FILE_NAME)->List[str]:
    requirements =[]

    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

    if  HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)

    return requirements       

setup(
    name = NAME,
    version = VERSION,
    auther = AUTHER,
    auther_email = AUTHER_EMAIL_ID,
    package = find_packages(),
    install_requires = get_requirments()
)