#!/bin/bash

if [ $# -lt 1 ] ; then
    echo -e "\nUsage: createimgsize [file] [optional:sizes]\n"
    exit
fi

file=$(basename -- "$1")
fext="${file#*.}"
fname="${file%.*}"

shift

[ $# != 0 ] && sizes="$@" || sizes="16 32 48 96"

for size in $sizes ; do
    lw="${size}x${size}"
    f="${fname}_${size}.${fext}"
    echo Creating resize of $lw on $f...
    convert "$file" -resize "$lw" "$f"
    echo $f created!
done
