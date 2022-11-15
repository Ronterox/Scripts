#!/bin/bash

function check_trash()
{
    while getopts 't' opt ; do
        if [ "$opt" == t ] ; then
            trash="$@[$OPTIN]"
            return 2
        fi
    done
    return 0
}

trash=~/.local/share/Trash/files/ ; workdir="$(pwd)"
case $# in
    1) workdir=$1 ;;
    2) check_trash $@ ;;
    3) check_trash $@ ; shift $? ; workdir=$1 ; check_trash $@ ;;
esac

RED=31
GRN=32
CYN=36

function c() { echo "\e[$2m$1\e[0m"; }

function say()
{
    [ $# == 2 ] && w=$(c "$1" $2) || w="$1"
    echo -e "$w"
}

function menu()
{
    clear
    say "$vid" $CYN
    say "Left Key: Delete" $RED
    say "Right Key: Continue" $GRN
    say "Up Key: History" 35
    say "\nDown Key: Quit" 34
}

function show_h() { say "\nHistory ~\n" && say "$files"; }

while read vid
do
    clear
    say "Watching $vid\n" $CYN
    mpv --loop-file=no --loop-playlist=no --keep-open=no "$vid"

    menu
    while true; do
        read -n 1 k <&1
        menu
        if [ $? == 0 ]; then
            case "$k" in
                C) files+="$(c "$vid" $CYN)\n" ; break;;
                D)
                    say "\nDeleting $vid..." $RED
                    rsync --remove-source-files -P "$vid" "$trash"
                    say "\n$vid deleted successfully!" $GRN
                    files+="$(c "$vid" $RED)\n"
                    break;;
                A) show_h ;;
                B) say "Closing app...\n" && exit ;;
            esac
        fi
    done
done <<< $(find "$workdir" -name '*.mp4')

show_h
say "Video checking finished successfully!\n" $GRN
