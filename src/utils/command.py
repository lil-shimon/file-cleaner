import sys  # コマンド引数を取得するため使用

from clean_desktop import clean_handler  

def check_args():
  """
  コマンドに引数を指定しているか確認
  指定している場合は特定の動作に移る。
  ない場合は選択肢を表示 
  """

  args = sys.argv
  if 1 <= len(args):
    print('args')
  else:
    clean_handler()