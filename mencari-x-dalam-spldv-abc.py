import math
while True:
  def cari(a, b, c):
    d = math.sqrt(b**2 - 4*a*c)
    x1 = (-b - d) / (2 * a)
    x2 = (-b + d) / (2 * a)
    return x1, x2

  a = int(input("a: "))
  b = int(input("b: "))
  c = int(input("c: "))

  x1, x2 = cari(a, b, c)
  print("x1=",x1)
  print("x2=",x2)
