l =float(input ("Informe a quantidade de litros comprados: "))
tipo = str(input("Digite (A) para alcool e (G) para gasolina: "))
if tipo == "A":
	preco = 3.4
	if l <= 20:
		desc = 3
	elif l > 20:
		desc = 5
elif tipo == "G":
	preco = 4.5
	if l <= 20:
		desc = 4
	elif l > 20:
		desc = 6
total = int(l * preco - (l * preco * desc / 100))
print ("O valor total a ser pago por {} litros de {} é: R$ {}".format (l, tipo, total
))