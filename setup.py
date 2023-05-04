from setuptools import setup, find_packages

setup(
    name='typyd',
    description='Python type enforcer',
    long_description='Python type enforcer',
    packages=find_packages(exclude=["*tests*"]),
    version='1.0.9',
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
