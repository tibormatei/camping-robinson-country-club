#!/usr/bin/env bash
set -e  # Exit immediately if any command fails

cd ..

# Run all tests
echo "Run all Model tests"
python -m unittest test/test_TentModel.py
python -m unittest test/test_TrailerModel.py
python -m unittest test/test_TrailersModel.py
python -m unittest test/test_DogModel.py

echo ""
echo "Run all View tests"
python -m unittest test/test_TentView.py
python -m unittest test/test_TrailerView.py
python -m unittest test/test_DogView.py

echo ""
echo "Run all data tests"
python -m unittest test/test_RentalDetailsDataFromFile.py
