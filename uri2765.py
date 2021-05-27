while True:
  try:
    a,b = input().split(',')
    print(a)
    print(b)
  except EOFError:
    break
