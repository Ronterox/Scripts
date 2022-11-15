path=$@
if [ $# = 0 ]; then
 path=$(pwd)
fi
cd $(dirname $(realpath $0))
./main.py "$path"
