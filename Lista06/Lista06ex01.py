matriz = [[ ], [ ], [ ], [ ]]
cont = 0
for i in range(0,4):
	for j in range(0,4):
		matriz[i].append(int(input(f"Digite um valor para [{i}, {j}]: ")))
print('-='*30)
for i in range(0,4):
	for j in range(0,4):
		print(f"[{matriz[i][j]: ^5}]",end= " ")
	print()
for i in range(0,4):
	for j in range(0,4):
            if(matriz[i][j] > 10):
            	cont = cont + 1
print("Existem na matriz %d números maiores que 10."%cont)
