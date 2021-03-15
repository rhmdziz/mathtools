while True:
  def derajat3():
    bagi = int(input("bagi: ")
    a = int(input("a: "))
    b = int(input("b: "))
    c = int(input("c: "))
    b = b - (a*bagi)
    x = c - (b*bagi)
    return bagi, x
  def derajat4():
    d = int(input("d: "))
    x = d - (x*bagi)
    return x
  def derajat5():
    e = int(input("e: "))
    x = e - (x*bagi)
    return x
  def derajat6():
    f = int(input("f: "))
    x = f - (x*bagi)
    return x
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
  #  dah nanti aja
  print(x)
