matriz = [[ ], [ ], [ ], [ ],[ ]]
cont = 0
for i in range(0,5):
	for j in range(0,5):
		matriz[i].append(int(input(f"Digite um valor para [{i}, {j}]: ")))
print('-='*30)
for i in range(0,5):
	for j in range(0,5):
		print(f"[{matriz[i][j]: ^5}]",end= " ")
	print()
	
num = int(input("Pesquisar um numero: "))

for i in range(0,5):
	for j in range(0,5):
		if(matriz[i][j] == num):
			cont = 1
if cont == 1:
	print("O valor encontrado é %d na posição %d %d \n" %(num, i, j))
else:
	print("Valor não encontrado.")

