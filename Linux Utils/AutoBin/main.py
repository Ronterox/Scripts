#!/bin/python3
from sys import argv

if len(argv) == 4:
    import os

    run_path = argv[1] + "/run.sh"
    link_path = '/usr/bin/' + argv[3]

    with open(run_path, 'w') as f:
        code = 'cd $(dirname $(realpath $0))\n' + argv[2] + ' \"$@\"'
        f.write(code)
        print(code)

    os.chmod(run_path, 0o755)
    os.symlink(run_path, link_path)
else:
    # autobin <path> <exec> <name>
    print("\nTry: autobin <exec> <name>\n")
