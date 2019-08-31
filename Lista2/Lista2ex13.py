valor = int (input("Informe o valor que deseja sacar: "))
if valor < 10 or valor > 600:
	print ("Valor inválido")
else:
	cem = int(valor / 100)
	valor = valor - (cem*100)
	cinquenta = int(valor /50)
	valor = valor  - (cinquenta*50)
	dez = int(valor/10)
	valor = valor - (dez*10)
	cinco = int(valor/5)
	valor = valor  - (cinco*5)
	um = valor 
	print('Notas de R$100,00 = ',cem)
	print('Notas de R$ 50,00 = ',cinquenta)
	print('Notas de R$ 10,00 = ',dez)
	print('Notas de R$  5,00 = ',cinco)
	print('Notas de R$  1,00 = ',um)
