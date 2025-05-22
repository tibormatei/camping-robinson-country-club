#!/usr/bin/env bash
set -e  # Exit immediately if any command fails

cd ..

# Run all tests
python -m unittest test/test_TentModel.py
python -m unittest test/test_TrailerModel.py
python -m unittest test/test_TrailersModel.py
python -m unittest test/test_DogModel.py
