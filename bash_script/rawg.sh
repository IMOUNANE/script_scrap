#!/bin/bash
rm -rf virtualenv || true
rm -rf action_rawg_pyhton.zip || true
wsk action delete rawg || true


script_dir=$(dirname "$0")

cd "$script_dir/../actions/scrap/rawg"

virtualenv virtualenv

. ./virtualenv/bin/activate

pip install bs4
pip install requests

deactivate

zip -r action_rawg_pyhton.zip virtualenv __main__.py

wsk action create rawg --kind python:3.7 --main main action_rawg_pyhton.zip