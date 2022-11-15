#!/bin/bash

if [ $# -lt 2 ]; then
    echo -e "\nUsage: pullout [ftype] [path]\n"
    exit
fi

ftype="*$1"

shift
echo Moving files of type $ftype to $@

find "$@" -name "$ftype" | while read -r f
do
    mv -t "$@" "$f"
done
