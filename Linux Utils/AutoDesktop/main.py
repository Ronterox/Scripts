#!/bin/python3
from sys import argv, stdout


def create_template(name, root="/usr/share/applications/"):
    from shutil import copyfile

    path = root + name.replace(' ', '-') + '.desktop'
    copyfile('template.desktop', path)

    return path


def get_template(path):
    from configparser import RawConfigParser

    template = RawConfigParser()
    template.optionxform = str
    template.read(path)

    return template


class PathHandler:
    def __init__(self, args):
        self.args = args

    def get_path(self, param):
        from os.path import abspath, exists

        try:
            fname = self.args[param]
            path = abspath(fname) if fname.__contains__('.') else fname
            if fname.__contains__('.') and not exists(path):
                print("[Error]: File doesn't exist", path)
            else:
                return path
        except KeyError as e:
            print("[Error]: Missing argument", e)
        raise Exception("Fix the path...")


def get_params(args):
    handler = PathHandler(args)

    name = args[1]
    comment = args[2]
    execute = handler.get_path(3)
    icon = handler.get_path(4)
    terminal = "true" if len(args) > 5 else "false"

    return name, comment, execute, icon, terminal


def edit_file(template, name, comment, execute, icon, terminal="false"):
    ref = template["Desktop Entry"]
    ref["Name"] = name
    ref["Exec"] = execute
    ref["Icon"] = icon
    ref["Comment"] = comment
    ref["Terminal"] = terminal


def save_changes(template, path):
    with open(path, 'w') as f:
        template.write(f, space_around_delimiters=False)
        template.write(stdout, space_around_delimiters=False)


def read_file(args):
    try:
        name, comment, execute, icon, terminal = get_params(args)

        path = create_template(name)
        template = get_template(path)

        edit_file(template, name, comment, execute, icon)
        save_changes(template, path)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    if len(argv) > 4:
        read_file(argv)
    else:
        print("\nTry: autodesktop <name> <comment> <exec> <icon> <terminal(optional)>\n")
