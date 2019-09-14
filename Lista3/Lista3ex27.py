cont = 0
soma = 0
N = int(input ("Digite um número: "))
while cont < N:
	cont = cont + 1
	H= (1/cont)
	print ("%.2f" %H)
	soma = soma + H
print ("O resultado total será: %.2f" %soma)
