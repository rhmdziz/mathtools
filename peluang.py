import random

l = ["1","2","3","4","5","6","7","8","9","A","B","C","D","E","F","G","H","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

codes = []

while True:
	a = random.choice(l)
	b = random.choice(l)
	c = random.choice(l)
	d = random.choice(l)
	e = random.choice(l)
	f = random.choice(l)
	
	code = a+b+c+d+e+f
	
	if code not in codes:
	  codes.append(code)
	  
	  
	  print(len(codes),"#"+code)
