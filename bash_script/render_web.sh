wsk action delete render_web || true

script_dir=$(dirname "$0")

wsk action create render_web $script_dir/../actions/main.js