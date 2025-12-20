from setuptools import find_packages , setup
from typing import List


var_a = '-e .'
def get_requirements(file_path:str) -> List[str]:

    requirements=[]
    with open (file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","")for req in requirements]

        if var_a in requirements:
            requirements.remove(var_a)
    
    return requirements

setup(
    name="mlproject",
    version='0.0.1',
    author= 'Akshit',
    author_email='akshitis@gmail.com',
    packages = find_packages(),
    install_requires =get_requirements('requirements.txt')
)