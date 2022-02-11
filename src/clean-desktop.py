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


def check_mkdirs(path):
    """
    フォルダが存在していなかったら作成する関数
    :param path: string
    :return:
    """

    # もしフォルダがなかったら作成する
    if not os.path.isdir(path):
        print('初めての実行ですね。デスクトップのファイルをBackUpするためにバックアップフォルダを作成しました')
        os.makedirs(path)


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
        shutil.move(file, path)
        print(file + "が移動完了しました。。。。")


def clean_desktop_handler():
    """
    デスクトップをきれいにする関数

    :return: void
    """

    home_dir = get_dir_path("~")  # ホームディレクトリを取得
    backup_path = home_dir + "/desktop-backups"  # デスクトップファイルPath
    check_mkdirs(backup_path)  # バックアップがあるか確認し、なかったら作成

    desktop_path = get_dir_path("~/Desktop")  # Desktopフォルダパス
    desktop_files = get_file_info_from_folder(desktop_path + "/*")  # Desktopにあるファイルを取得

    if not desktop_files:  # デスクトップに何もない場合
        print("デスクトップはとてもきれいです！")
        return
    else:  # 移動できるファイルがある場合
        move_to_backup(desktop_files, backup_path)


if __name__ == "__main__":
    clean_desktop_handler()
