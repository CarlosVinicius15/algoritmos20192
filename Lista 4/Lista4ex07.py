ch = input("Caractere: ")
coluna = ordem = int(input("Digite a ordem da matriz para desenhar o triangulo: "))
for linha in range(0,ordem):
	for coluna in range(0,coluna):
		print(ch, end = ' ')
	print()