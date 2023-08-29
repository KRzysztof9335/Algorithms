SHELL := /bin/bash

root := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))
venv := $(root)/.venv
requirements := $(root)/requirements.txt

dirs := $(root)/CodingGame/easy
dirs += $(root)/CodingGame/medium
dirs += $(root)/CodingGame/hard

pylint := $(venv)/bin/pylint
pycodestyle := $(venv)/bin/pycodestyle

venv: $(venv)/timestamp
$(venv)/timestamp: $(requirements)
	echo "Creating venv"
	test -d $(venv) || python3 -m venv $(venv)
	source $(venv)/bin/activate; python -m pip install --upgrade pip; python3 -m pip install -r $(requirements)
	touch $(venv)/timestamp


pylint: venv
	$(pylint) $(dirs)

pycodestyle: venv
	$(pycodestyle) $(dirs) --ignore=E501  # Ignore too long line

static: pylint pycodestyle

test: static