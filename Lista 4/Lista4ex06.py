ch = input("Caractere: ")
ordem = int(input("Digite a ordem da matriz para desenhar o triangulo: "))
for coluna in range(0,ordem):
	for linha in range(0,coluna + 1):
			print(ch, end = " ")
	print()
	