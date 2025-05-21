#!/usr/bin/env bash
set -e  # Exit immediately if any command fails

cd ..

# Run all tests
python -m unittest test/test_TentModel.py
