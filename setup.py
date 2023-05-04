import codecs

from setuptools import setup, find_packages


# -*- Long Description -*-


def long_description():
    try:
        return codecs.open('README.md', 'r', 'utf-8').read()
    except OSError:
        return 'Long description error: Missing README.rst file'


setup(
    name='typyd',
    description='Python type enforcer',
    long_description=long_description(),
    packages=find_packages(exclude=["*tests*"]),
    version='1.1.0',
    install_requires=[
        'wheel'
    ],
    extras_require={
        'dev': [
            'pycodestyle',
            'flake8',
            'twine>=4.0.2',
        ],
    }
)
