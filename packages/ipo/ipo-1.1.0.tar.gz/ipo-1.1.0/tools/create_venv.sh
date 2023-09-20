#!/bin/bash

# © 2020, Midgard
# License: GPL-3.0-or-later
# This file is not available under the LGPL!

set -euo pipefail

cd $(dirname "$0")/..

# Create virtualenvs
if [ "${1:-}" = v ]; then
	virtualenv -p 3.8  venv3.8/
	virtualenv -p 3.9  venv3.9/
	virtualenv -p 3.10 venv3.10/
	virtualenv -p 3.11 venv3.11/
	virtualenv -p pypy3 venvpypy3/
	ln -s venv3.11 venv
else
	python -m virtualenv venv/
fi

# Install dependencies

if [ "${1:-}" = v ]; then
	venv3.8/bin/pip install -e .
	venv3.9/bin/pip install -e .
	venv3.10/bin/pip install -e .
	venv3.11/bin/pip install -e .
	venvpypy3/bin/pip install -e .
else
	venv/bin/pip install -e .
fi
