vetor = [10]
cont = 0
for i in range (0,10):
	valor = int(input ("Digite 10 valores: "))
	vetor.append(valor)
	if valor % 2 == 0:
		cont = cont + 1
print ("Existem %d valores pares" %cont)