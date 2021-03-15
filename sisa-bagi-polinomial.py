while True:
  def derajat3():
    bagi = int(input("bagi: ")
    a = int(input("a: "))
    b = int(input("b: "))
    c = int(input("c: "))
    return bagi, a, b, c
  def derajat4():
    d = int(input("d: "))
    return d
  def derajat5():
    e = int(input("e: "))
    return e
  def derajat6():
    f = int(input("f: "))
    return f
  input_derajat = int(input("Berapa derajat(3--6): "))
  if input_derajat == 3:
    derajat3()
  elif input_derajat == 4:
    derajat3()
    derajat4()
  elif input_derajat == 5:
    derajat3()
    derajat4()
    derajat5()
  elif input_derajat == 6:
    derajat3()
    derajat4()
    derajat5()
    derajat6()
  else:
    print("error")
  b = b - (a*bagi)
  c = c - (b*bagi)

  #  dah nanti aja
  print(x)
