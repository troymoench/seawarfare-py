#!/usr/bin/env bash

set -e
set -x

black src tests --check
isort src tests --check
flake8 src tests --statistics
mypy src tests
