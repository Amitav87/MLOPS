from setuptools import find_packages,setup
from typing import List
Hypon_E_DOT= '-e .'
def get_requirements(file_path:str)->List[str]:
    '''This function will returns the list of requirements'''

    requirements= []
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()

        # Remove newline characters from each requirement
        requirements=[req.replace("\n", " ") for req in requirements]
        # Check if 'Hypon_E_DOT' is in the list, and remove it if present
        if Hypon_E_DOT in requirements:
            requirements.remove(Hypon_E_DOT)

    return requirements
    

setup(
    name="ml_project",
    version='0.0.1',
    author="amitav",
    author_email="kumar.amitav87@gmail.com",
    packages= find_packages(),
    install_requires=get_requirements('requirements.txt')


)