from setuptools import setup, find_packages
HYPHEN_E_DOT = "-e ."

def get_requirements(file_path: str)-> list[str]:
    with open(file_path) as f:
        requirements = f.readlines()
    requirements = [x.replace("\n", "") for x in requirements]
    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(
    name="My Project",
    author="yash",
    author_email="yashcgosavi@gmail.com",
    packages=find_packages(),
    version="0.0.1",
    requires=get_requirements("requirements.txt")
)