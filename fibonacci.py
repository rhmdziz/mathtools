while True:
  a = int(input('a: '))
  b = int(input('u2: '))
  print(a,b,+'endln=' ')
  for i in range(10):
    c = a + b
    a, b = b, c
    print(c)
