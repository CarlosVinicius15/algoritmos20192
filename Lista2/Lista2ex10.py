a = float(input("Valor de A: "))


if a == 0:
	print ("Essa equaçao não é do segundo grau")
else:
	b = float (input("Valor de B: "))
	c = float (input("Valor de C: "))
	delta = b**2 - 4 * a * c
	if delta < 0:
	  	print ("Não há raizes")
	elif delta == 0:
			x = (-b) / (2 * a)
			print ("Há uma raiz real:", x)
	else:
		x1 = ((-b) + (delta**(1/2))) / (2 * a)
		x2 = ((-b) - (delta**(1/2))) / (2 * a)
		print ("Há duas raizes reais: ", x1, "e", x2)
	
	

  
      				
	