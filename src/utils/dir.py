# coding: UTF-8

import glob
import os
import pathlib


def get_folder(path) -> object:
    """

    :rtype: object
    """
    files = os.listdir(path)
    return [f for f in files if os.path.isdir(os.path.join(path, f))]


def display_tree(path, layer=0, is_last=False, current_indent='　'):
    if not pathlib.Path(path).is_absolute():  # in case relative path
        path = str(pathlib.Path(path).resolve())  # convert from relative path to absolute

    current = path.split('/')[::-1][0]  # get current
    # display current dir
    if layer == 0:
        print("<" + current + ">")
    else:
        branch = "└" if is_last else "├"
        print('{indent}{branch}{dirname}'.format(indent=current_indent, branch=branch, dirname=branch))

    paths = [p for p in glob.glob(path + '/*') if
             os.path.isdir(p) or os.path.isfile(p)]  # get path of other folders, files

    def is_last_path(i):
        return i == len(path) - 1

    # display recursively
    for i, p in enumerate(paths):
        indent_lower = current_indent
        if layer != 0:
            indent_lower += '　　' if is_last else '│　'
        if os.path.isdir(p):
            display_tree(p, layer=layer + 1, is_last=is_last_path(i), current_indent=indent_lower)
        if os.path.isfile(p):
            branch = '└' if is_last_path(i) else '├'
            print(
                '{indent}{branch}{filename}'.format(indent=indent_lower, branch=branch, filename=p.split('/')[::-1][0]))


def ask_display_tree(path):
    opt = input()

    if opt == "yes" or opt == "y":
        print("最終的にフォルダはこのようなフォルダ構成になりました")
        print(display_tree(path))
