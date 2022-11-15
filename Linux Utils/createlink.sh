if [ $# != 2 ] ; then
    echo Usage: [orgfile] [targfile]
else
    ln -s "$(realpath "$1")" "$2"
fi
