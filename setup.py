from setuptools import setup

setup(
    name='py-typed',
    description='Python type enforcer',
    long_description='Python type enforcer',
    packages=['py_typed'],
    version='1.0.0',
    install_requires=[
        'typing>=3.5.0,<3.11',
        'wheel'
    ],
    extras_require={
        'dev': [
            'pycodestyle',
            'flake8',
        ],
    }
)
