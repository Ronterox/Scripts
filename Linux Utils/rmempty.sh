[ $# == 0 ] && path="$(pwd)" || path="$@"

find "$path" -type d -empty -exec rmdir {} \;
