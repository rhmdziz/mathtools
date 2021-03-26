a = int(input('a : '))
b = int(input('u2: '))
d = int(input('un: '))
print(a, b, end=' ')
for i in range(d-2):
  c = a + b
  a, b = b, c
  print(c, end=' ')
