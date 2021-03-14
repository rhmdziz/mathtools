import math
while True:
  def cari(a, b, c):
    d = math.sqrt(b**2 - 4*a*c)
    x1 = (-b - d) / (2 * a)
    x2 = (-b + d) / (2 * a)
    print(x1, x2)
  a = int(input("a: "))
  b = int(input("b: "))
  c = int(input("c: "))
  cari(a, b, c)
