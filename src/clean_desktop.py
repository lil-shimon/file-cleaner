# coding: UTF-8

import glob  # フォルダ情報取得のため
import os
import shutil  # ファイル移動のため
from os.path import expanduser  # ホームディレクトリ取得のため
import sys  # コマンドを受け取るため
from utils.command import args_handler  
from utils.dir import ask_display_tree  # フォルダ一覧取得


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
        print("path", path)
        try:
            os.makedirs(path)
        except FileExistsError:
            return
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
            folder_path = path + "/folder"
            check_mkdirs(folder_path)
            shutil.move(file, folder_path)
            return
        if ext:
            backup_path_by_extension = path + "/" + ext  # ファイルごとのバックアップフォルダ
            # 拡張子のバックアップフォルダが存在していなかったら作成する
            check_mkdirs(backup_path_by_extension,
                         "新しい拡張子が掃除対象になりました。フォルダを作成します")
            try:
                shutil.move(file, backup_path_by_extension)
            except shutil.Error:
                print(file, "が移動できませんでした")

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
    # バックアップがあるか確認し、なかったら作成
    check_mkdirs(
        backup_path, '初めての実行ですね。デスクトップのファイルをBackUpするためにバックアップフォルダを作成しました')

    desktop_path = get_dir_path("~/Desktop")  # Desktopフォルダパス
    desktop_files = get_file_info_from_folder(
        desktop_path + "/*")  # Desktopにあるファイルを取得

    if not desktop_files:  # デスクトップに何もない場合
        print("デスクトップはとてもきれいです！")
        return
    else:  # 移動できるファイルがある場合
        move_to_backup(desktop_files, backup_path)


def clean_backup_handler():
    """
    バックアップフォルダをきれいにする関数
    :return:
    """

    backup_path = get_dir_path("~") + '/desktop-backups'  # backup path
    backup_files = get_file_info_from_folder(
        backup_path + "/*")  # backup files

    if not backup_files:
        print("バックアップフォルダはとてもきれいです！")
        return
    if backup_files:
        files = [f for f in backup_files if os.path.isfile(
            os.path.join(backup_path, f))]
        for file in files:
            ext = get_file_ext(file)  # get extension
            # 拡張子がない、変な形で保存されたファイルが存在するのでそういうものはスキップ
            if not ext:
                return
            backup_path_by_ext = backup_path + "/" + ext  # get proper backup path
            shutil.move(file, backup_path_by_ext)  # move file to proper dir
            print(file, "を移動しました")


def clean_download_handler():
    """
    ダウンロードフォルダをきれいにする関数
    :return:
    """

    root_path = get_dir_path("~")
    download_path = os.path.join(root_path, "Downloads")  # download path
    download_files = get_file_info_from_folder(
        download_path + "/*")  # download files

    print("ダウンロードフォルダ用のバックアップを作成しますか？ y/n [default: no]")
    cmd = input()
    if cmd == 'y' or cmd == "yes":
        print("この処理には時間がかかる可能性があります...")
        download_backup_path = root_path + "/download-backups"
        check_mkdirs(download_backup_path, "ダウンロード用のバックアップフォルダを作成しました。")
        try:
            # if there is download backup folder, delete it.
            shutil.rmtree(download_backup_path)
            # copy download folder into download backup folder
            shutil.copytree(download_path, download_backup_path)
            print("バックアップを作成しました")
        except FileExistsError:  # just in case
            return

    if not download_files:
        print("ダウンロードフォルダはとてもきれいです！")
        return

    files = [f for f in download_files if os.path.isfile(
        os.path.join(download_path, f))]  # check file exists

    for file in files:
        ext = get_file_ext(file)  # get extension
        if not ext:
            # for files or folders don't have extension
            folder_path = download_path + '/' + "/folder"
            check_mkdirs(folder_path)
            shutil.move(file, folder_path)
        if ext:
            download_path_by_ext = download_path + "/" + \
                ext  # full path (include extension data)
            # check folder by extension exists
            check_mkdirs(download_path_by_ext, "新しい拡張子なので、フォルダを作成します")
            shutil.move(file, download_path_by_ext)  # move file
        print(file, "を移動しました")

    print("掃除が終わりました!")
    print("ファイル構成を確認しますか？ yes/no [default=no]")
    ask_display_tree(download_path)


def select_act(cmd):
    if not cmd or int(cmd) == 1:
        clean_desktop_handler()
    if int(cmd) == 2:
        clean_backup_handler()
    if int(cmd) == 3:
        clean_download_handler()
    else:
        return


def clean_handler():
    args = sys.argv

    # 引数があった場合
    if 2 <= len(args):
        cmd = args_handler(args[1])
        if not cmd:
            return
        else:
            select_act(cmd)

    # 引数がない場合
    else:
        print('したい動作を選んでください')
        print('1. デスクトップをきれいにしたい [default]')
        print('2. バックアップフォルダを整理したい')
        print('3. ダウンロードフォルダを整理したい')
        cmd = input()
        select_act(int(cmd))


if __name__ == "__main__":
    clean_handler()
