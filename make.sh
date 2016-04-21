#!/bin/bash

# Delete old build
rm -rf dist/
rm ntbotPostIssue.zip

# Create our virtual environment
rm -rf env
virtualenv env
source env/bin/activate
pip install -r requirements.txt

# Create dist
cp -r src dist
cp -r env/lib/python2.7/site-packages/* dist/

cd dist

# Removed compiled pyc
rm -rf *.pyc
# Remove 20MB of fluff
rm -rf github/tests/ReplayData

# Zip up dist folder
zip -r ../ntbotPostIssue.zip .
cd ..
