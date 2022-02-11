import os
from os.path import expanduser  # ホームディレクトリ取得のため


def get_homedir():
    """
    ホームディレクトリを取得する関数
    :return: string
    """
    return expanduser("~")


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


def clean_desktop_handler():
    """
    デスクトップをきれいにする関数

    :return: void
    """

    home_dir = get_homedir()  # ホームディレクトリを取得
    path_to_backup = home_dir + "/desktop-backups"  # デスクトップファイルPath

    check_mkdirs(path_to_backup)


if __name__ == "__main__":
    clean_desktop_handler()
