#!/usr/bin/env bash
set -e  # Exit immediately if any command fails

cd "$(dirname "$0")"/..

# Run all tests
PYTHONPATH=. python -m unittest test/test_TentModel.py
