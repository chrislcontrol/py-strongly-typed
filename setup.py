from setuptools import setup

setup(
    name='typyd',
    description='Python type enforcer',
    long_description='Python type enforcer',
    packages=['typyd'],
    version='1.0.0',
    install_requires=[
        'typing<3.11',
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
