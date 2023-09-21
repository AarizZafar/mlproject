# WITH THIS setup.py FILE WE WILL BE ABLE TO CREATE OUR MACHINE LEARNIGN MODEL AS A PACKAGE AND WILL BE ABLE TO INSTALL IT ANY WHERE

# setuptools -> PYTHON PACKAGE THAT PROVIDES A FRAME WORK FOR BUILDING AND DISTRIBUTING PYTHON PACKAGES
from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    THIS FUNCTION WILL RETURN THE LIST OF REQUIREMENTS
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    

setup (
    name                      =       'mlproject',
    verision                  =       '0.0.1',
    author                    =       'Aariz',
    author_mail               =       'aariz.zafar01@gmail.com',
    packages                  =        find_packages(),            # find_packages -> WILL FIND ALL THOSE FOLDERS THAT HAVE __init__.py 
    install_requirements      =        get_requirements("requirements.txt") 
)