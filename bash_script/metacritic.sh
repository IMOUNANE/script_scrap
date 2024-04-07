rm -rf virtualenv || true
rm -rf action_metacritic_pyhton.zip || true
wsk action delete metacritic || true



script_dir=$(dirname "$0")

cd "$script_dir/../actions/scrap/metacritic"

virtualenv virtualenv

. ./virtualenv/bin/activate

pip install langdetect
pip install requests

deactivate

zip -r action_metacritic_pyhton.zip virtualenv __main__.py

wsk action create metacritic --kind python:3.7 --main main action_metacritic_pyhton.zip
