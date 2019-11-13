matriz = []
ordem = int(input("Ordem da matriz: "))
for i in range(ordem):
  matriz.append([0]*ordem)
for i in range(ordem):
  for j in range(ordem):
    matriz[i][j] = int(input("A[" + str(i+1) + "][" + str(j+1) + "]:"))
for i in range(ordem):
  for j in range(ordem):
      print(f'[{matriz[i][j]}]',end=" ")
  print()
somaabaixo = 0
for i in range(ordem):
 for j in range(ordem):
   if i > j:
    somaabaixo = somaabaixo + matriz[i][j]  
print("A soma da parte debaixo da diagonal principal é", somaabaixo)