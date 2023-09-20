#!/bin/bash

# © 2020, Midgard
# License: GPL-3.0-or-later
# This file is not available under the LGPL!

cd $(dirname "$0")/..

if ! ( test -d venv3.8 && test -d venv3.9 && test -d venv3.10 && test -d venv3.11 ); then
	echo "Versioned virtualenvs not found, creating them first"
	tools/create_venv.sh v
fi

venv3.8/bin/pip install pytest
venv3.9/bin/pip install pytest
venv3.10/bin/pip install pytest
venv3.11/bin/pip install pytest

venv3.8/bin/pytest ./tests
venv3.9/bin/pytest ./tests
venv3.10/bin/pytest ./tests
venv3.11/bin/pytest ./tests
