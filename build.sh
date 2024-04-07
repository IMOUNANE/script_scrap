#!/bin/bash
# delete all for init config
wsk action delete render_web || true

script_dir=$(dirname "$0")

# dataset script
sh $script_dir/bash_script/metacritic.sh
sh $script_dir/bash_script/rawg.sh

#render_web
wsk action create render_web $script_dir/actions/main.js

sh $script_dir/bash_script/sequence.sh

