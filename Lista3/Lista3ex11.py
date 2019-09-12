par = 0
impar = 0
cont = 0
while cont < 10:
	num = int(input("Digite um número: "))
	cont += 1
	if num % 2 == 0:
		par += 1
	else:
		impar += 1
print ("O total de Pares é:", par, "\nO total de Ímpares é:", impar)