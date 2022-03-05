#!/usr/bin/env bash

set -e
set -x

black src tests
isort src tests
