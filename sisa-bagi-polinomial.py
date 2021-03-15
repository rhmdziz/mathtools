while True:
  def operasi():
    bagi = int(input("bagi: "))
    a = int(input("a: "))
    b = int(input("b: "))
    c = int(input("c: "))
    d = int(input("d: "))
    b = b - (a*bagi)
    c = c - (b*bagi)
    d = d - (c*bagi)
    if input_derajat == 3:
        print('sisa bagi:',d,'\n')
    elif input_derajat == 4:
        e = int(input("e: "))
        e = e - (d*bagi)
        print('sisa bagi',e, '\n')
    elif input_derajat == 5:
        e = int(input('e: '))
        e = e - (d*bagi)
        f = int(input('f: '))
        f = f - (e*bagi)
        print('sisa bagi:',f,'\n')
    elif input_derajat == 6:
        e = int(input('e: '))
        e = e - (d*bagi)
        f = int(input('f: '))
        f = f - (e*bagi)
        g = int(input('g: '))
        g = g - (f*bagi)
        print('sisa bagi:',g,'\n')
  input_derajat = int(input("Berapa derajat(3--6): "))
  if input_derajat == 3 or input_derajat == 4 or input_derajat == 5 or input_derajat == 6:
    operasi()
  else:
    print("error\n")
