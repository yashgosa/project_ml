from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = "-e ."

def find_requirements(file_path: str) -> List[str]:
    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [x.replace("\n", "") for x in requirements]
        
    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)
    return requirements

# print(find_requirements("requirements.txt"))

setup(
    name="ML Project",
    author="yash gosavi",
    author_email="yashcgosavi@gmail.com",
    requires=find_requirements("./requirements.txt"),
    packages=find_packages()
)