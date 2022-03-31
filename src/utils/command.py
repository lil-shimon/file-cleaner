def args_handler(args):
  """
  コマンド引数によって処理を分割する関数
  -dはデスクトップ
  """

  if args == "-d":
    return 1
  else:
    print("未対応です")
    return