import glob
import os
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

    files = glob.glob(path)
    print("現在、デスクトップはこのようになっています")
    for file in files:
        print(file)


def clean_desktop_handler():
    """
    デスクトップをきれいにする関数

    :return: void
    """

    home_dir = get_dir_path("~")  # ホームディレクトリを取得
    backup_path = home_dir + "/desktop-backups"  # デスクトップファイルPath
    check_mkdirs(backup_path)  # バックアップがあるか確認し、なかったら作成

    desktop_path = get_dir_path("~/Desktop")  # Desktopフォルダパス
    get_file_info_from_folder(desktop_path + "/*")


if __name__ == "__main__":
    clean_desktop_handler()
