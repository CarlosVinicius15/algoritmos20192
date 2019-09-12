ultimo = 1
penultimo = 1
cont = 2
num = int(input("Digite até que termo quer verificar: "))
if num == 1:
		print("1")
elif num == 0:
		print("0")
else:
	print(ultimo)
	print(penultimo)
	while cont != num:
		termo = ultimo + penultimo
		penultimo = ultimo
		ultimo = termo
		cont = cont + 1
		print(termo)
		
      