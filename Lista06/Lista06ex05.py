matriz = []
ordem = int(input("Ordem da matriz a ser criada: "))
for i in range(ordem):
  matriz.append([0]*ordem)
for i in range(ordem):
  for j in range(ordem):
    matriz[i][j] = int(input("A[" + str(i+1) + "][" + str(j+1) + "]: "))
for i in range(ordem):
  for j in range(ordem):
      print([matriz[i][j]],end=" ")
  print()
soma_acima = 0  
for i in range(ordem):
 for j in range(ordem):
   if j > i:
    soma_acima = somaacima + matriz[i][j]
print("A soma da parte acima da diagonal principal é",soma_acima)