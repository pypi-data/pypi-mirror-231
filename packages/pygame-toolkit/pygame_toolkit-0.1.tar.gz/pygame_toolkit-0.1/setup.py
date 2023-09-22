from setuptools import setup, find_packages

setup(
    name='pygame_toolkit',
    version='0.1',
    description='A collection of tools for use with Pygame',
    author='Vinicius Putti Morais',
    author_email='viniputtim@gmail.com',
    packages=find_packages(),
    install_requires=[
        'pygame',
    ],
)
