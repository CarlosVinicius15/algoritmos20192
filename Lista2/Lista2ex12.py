numero = int (input("Digite um número menor que 1000: "))
c = numero // 100
d = int (numero % 100 / 10)
u = numero % 100 % 10
if numero > 999 or numero < 0:
	print ("Valor inválido")
elif c == 0 and d == 0 and u == 0:
	print ("Zero não pode.")
elif c == 0 and d == 0 and u == 1:
	print("Esse número tem só uma unidade.")
elif c == 0 and d == 1 and u == 1:
	print("Esse número tem 1 dezena e 1 unidade.")
elif c == 0 and d > 1 and u == 1:
	print("Esse número tem", d, "dezenas e 1 unidade.")
elif c == 0 and d == 1 and u > 1:
	print ("Esse número tem 1 dezena e", u, "unidades.")
elif c == 1 and d == 0 and u == 0:
	print("Esse número tem 1 centena.")
elif c == 1 and d == 0 and u == 1:
	print ("Esse numero tem 1 centena e 1 unidade.")
elif c == 1 and d == 1 and u == 0:
	print ("Esse número tem 1 centena e 1 dezena.")
elif c == 1 and d == 1 and u == 1:
	print ("Esse número tem 1 centena, 1 dezena e 1 unidade.")
elif c == 1 and d > 1 and u > 1:
	print ("Esse número tem 1 centena, ",d, "dezenas e", u, "unidades.")
elif c > 1 and d == 1 and u == 1:
	print ("Esse número tem,", d, "dezenas, 1 centena e 1 unidade.")
elif c > 1 and d == 0 and u == 1:
	print ("Esse número tem", c, "centenas e 1 unidade.")
elif c > 1 and d == 0 and u == 0:
	print ("Esse número tem", c, "centenas.")
elif c > 1 and d == 0 and u > 1:
	print ("Esse número tem", c, "centenas e ", u, "unidades.")
elif c > 1 and d == 1 and u == 0:
	print ("Esse número tem", c, "centenas e 1 unidade.")
elif c > 1 and d > 1 and u == 0:
	print ("Esse número tem", c, "centenas e", d, "dezenas.")
elif c > 1 and d > 1 and u == 1:
	print ("Esse número tem", d, "centenas, ", d, "dezenas e 1 unidade.")
elif c > 1 and d > 1 and u > 1:
	print ("Esse número tem", c, "centenas,", d, "dezenas e", u, "unidades.")
elif c == 0 and d == 0 and u > 1:
	print ("Esse número tem", u, "unidades.")
elif c == 0 and d > 1 and u > 1:
	print ("Esse número tem", d, "dezenas e", u, "unidades.")
elif c == 0 and d == 1 and u == 0:
	print ("Esse número tem 1 dezena.")
elif c == 0 and d > 1 and u == 0:
	print ("Esse número tem", d, " dezenas")
	
	