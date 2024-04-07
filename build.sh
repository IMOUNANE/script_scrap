#!/bin/bash

script_dir=$(dirname "$0")

# script bash for create action
sh $script_dir/bash_script/metacritic.sh
sh $script_dir/bash_script/rawg.sh
sh $script_dir/bash_script/render_web.sh

# script bash for create sequence
sh $script_dir/bash_script/sequence.sh

