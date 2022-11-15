#!/bin/python3
import os

fileTypes = {}


def convert_type_length(to_convert, max_length):
    size_of = len(to_convert)
    if size_of < max_length:
        for _ in range(max_length - size_of):
            to_convert += ' '
    return to_convert


def convert_bytes(bytes):
    bytes = float(bytes)
    if bytes >= 1099511627776:
        terabytes = bytes / 1099511627776
        size = '%.2fT' % terabytes
    elif bytes >= 1073741824:
        gigabytes = bytes / 1073741824
        size = '%.2fG' % gigabytes
    elif bytes >= 1048576:
        megabytes = bytes / 1048576
        size = '%.2fM' % megabytes
    elif bytes >= 1024:
        kilobytes = bytes / 1024
        size = '%.2fK' % kilobytes
    else:
        size = '%.2fb' % bytes
    return size


def files_size(path):
    print(f'Directory: {path}\n')
    for root, dirs, files in os.walk(path):
        for name in files:
            path = os.path.join(root, name)
            f_type = os.path.splitext(name)[1]
            if f_type == '':
                continue
            elif f_type not in fileTypes:
                fileTypes[f_type] = os.path.getsize(path)
            else:
                fileTypes[f_type] += os.path.getsize(path)

    print('Type\tSize')
    total_size = 0
    for type, value in sorted(fileTypes.items(), key=lambda x: x[1], reverse=True):
        print(f'{convert_type_length(type, 4)}\t= {convert_bytes(value)}')
        total_size += value
    print(f'\nTotal directory size of {convert_bytes(total_size)}')


if __name__ == '__main__':
    from sys import argv
    files_size(argv[1])
    input('\nPress enter to continue...')

