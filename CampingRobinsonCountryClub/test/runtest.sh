#!/usr/bin/env bash
set -e  # Exit immediately if any command fails

# Run all tests
# -s : looks in current directory
python -m unittest -s test_TentModel.py