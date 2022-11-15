path=$(pwd)
cd $(dirname $(realpath $0))
sudo python3 main.py ${path} "$@"