#!/bin/bash

if [ $# -lt 2 ] ; then
    echo "Missing arguments!"
    echo "Usage: watchfile [file] [action]"
    exit
fi

path=$1
tmp=$(mktemp)
chmod +x "$tmp"

shift

args="$@"

echo "$args" > $tmp
echo "read line" >> $tmp

function run_instance() 
{ 
    killall gnome-terminal-server 2>/dev/null
    echo "$args" && gnome-terminal -- $tmp
}

file=$(cat $path)

while true; do
    clear
    read -t 1 -n 1 k<&1

    if [ $? == 0 ] && [ "$k" == "" ] ; then
        run_instance 
    else 
        new=$(cat $path)
        if [ "$file" != "$new" ] ; then
            file=$new
            run_instance
        else echo Watching $path...; fi
    fi

    sleep 1s
done

rm $tmp
