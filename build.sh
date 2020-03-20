#!/usr/bin/env bash

set -e

# clean up existing archive and build dir
rm -rf build
rm -f *.zip

echo "Building rm-webscrape ....."

# make build dir
mkdir build && cd build
touch __init__.py
cd ../

# copy contents of main code
cp -r src build/

# install python dependencies
pip3 install -r requirements.txt -t build/

# make archive in project's root directory
python3 -m zipfile -c rm-webscrape.zip build/*

echo "build completed and rm-webscrape.zip has been generated"

# remove build dir
rm -rf build
