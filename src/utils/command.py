def args_handler(args):
  """
  コマンド引数によって処理を分割する関数
  -dはデスクトップ
  """

  if args == "-h":
    return 1
  if args == "-b":
    return 2
  if args == "-d":
    return 3
  else:
    print("未対応です")
    return