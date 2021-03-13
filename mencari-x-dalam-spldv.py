while True:
  print("± aX^2 ± bX ± c")
  a = int(input("a: "))
  b = int(input("b: "))
  c = int(input("c: "))

  def operasi():
    for x1 in range(-100,100):
      for x2 in range(-100,100):
        if x1+x2==b and x1*x2==c:
          x1 *= -1
          x2 *= -1
          if a != 1:
            x1 /= a
            x2 /= a
            print("\nx1=",x1,"\nx2=" ,x2)
          else:
            print("\nx1=",x1,"\nx2=", x2)

  if a == 1:
    operasi()
  elif a == -1:
    a *= -1
    b *= -1
    c *= -1
    operasi()
  elif a > 1:
    b *= a
    c *= a
    operasi()
  elif a < -1:
    a *= -1
    b *= -1
    c *= -1
    b *= a
    c *= a
    operasi()
