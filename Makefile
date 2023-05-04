PROJECT_NAME := py-strongly-typed
PYTHON_VERSION := 3.10.4
VENV_NAME := $(PROJECT_NAME)-$(PYTHON_VERSION)

.pip:
	pip install pip --upgrade

setup: .pip
	pip uninstall -y typing
	pip install -U setuptools
	pip install -e .

setup-dev: .pip
	pip uninstall -y typing
	pip install -U setuptools
	pip install -e .[dev]

.setup-venv:
	pyenv install -s $(PYTHON_VERSION)
	pyenv uninstall -f $(VENV_NAME)
	pyenv virtualenv $(PYTHON_VERSION) $(VENV_NAME)
	pyenv local $(VENV_NAME)

create-venv: .setup-venv setup-dev

code-convention:
	flake8
	pycodestyle

create-dist:
	python setup.py sdist

upload-to-test:
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*

upload-to-production:
	twine upload dist/*
