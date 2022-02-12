# coding: UTF-8

import glob  # フォルダ情報取得のため
import os
import shutil  # ファイル移動のため
from os.path import expanduser  # ホームディレクトリ取得のため


def get_dir_path(path):
    """
    ディレクトリpathを取得する関数
    :return: string
    """
    return expanduser(path)


def check_mkdirs(path, message=None):
    """
    フォルダが存在していなかったら作成する関数
    :param path: string
    :param message: string?
    :return:
    """

    # もしフォルダがなかったら作成する
    if not os.path.isdir(path):
        os.makedirs(path)
        if message:
            print(message)


def get_file_info_from_folder(path):
    """
    フォルダ内のファイル、フォルダ一覧を取得
    :param path: string
    :return:
    """

    return glob.glob(path)


def move_to_backup(files, path):
    """
    fileを特定のディレクトリに移動する関数
    :param files:
    :param path:
    :return:
    """

    print("現在、デスクトップはこのようになっています")
    for file in files:
        print(file)

    print("デスクトップの掃除を開始します >>> ")
    for file in files:
        ext = get_file_ext(file)  # ファイル拡張子を取得
        if not ext:
            return
        backup_path_by_extension = path + "/" + ext  # ファイルごとのバックアップフォルダ
        check_mkdirs(backup_path_by_extension, f"新しい拡張子が掃除対象になりました。フォルダを作成します")  # 拡張子のバックアップフォルダが存在していなかったら作成する
        shutil.move(file, backup_path_by_extension)
        print(file + "が移動完了しました。。。。")


def get_file_ext(path):
    """
    ファイルの拡張子を取得
    :param path:
    :return: string
    """
    _, ext = os.path.splitext(path)
    return ext.replace(".", '')  # 先頭の.を取り除く


def clean_desktop_handler():
    """
    デスクトップをきれいにする関数

    :return: void
    """

    home_dir = get_dir_path("~")  # ホームディレクトリを取得
    backup_path = home_dir + "/desktop-backups"  # デスクトップファイルPath
    check_mkdirs(backup_path, '初めての実行ですね。デスクトップのファイルをBackUpするためにバックアップフォルダを作成しました')  # バックアップがあるか確認し、なかったら作成

    desktop_path = get_dir_path("~/Desktop")  # Desktopフォルダパス
    desktop_files = get_file_info_from_folder(desktop_path + "/*")  # Desktopにあるファイルを取得

    if not desktop_files:  # デスクトップに何もない場合
        print("デスクトップはとてもきれいです！")
        return
    else:  # 移動できるファイルがある場合
        move_to_backup(desktop_files, backup_path)


if __name__ == "__main__":
    clean_desktop_handler()
