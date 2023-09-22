from setuptools import setup, find_packages

setup(
    name='pygame_toolkit',
    version='0.3',
    description='Tools for use with pygame',
    author='Vinicius Putti Morais',
    author_email='viniputtim@gmail.com',
    packages=find_packages(),
    install_requires=[
        'pygame'
    ],
)
