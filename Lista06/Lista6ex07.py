matriz = []
ordem = int(input("Ordem da matriz: "))

for i in range(ordem):
  matriz.append([0]*ordem)
for i in range(ordem):
  for j in range(ordem):
    matriz[i][j] = int(input("a[" + str(i+1) + "][" + str(j+1) + "]:"))

for i in range(ordem):
  for j in range(ordem):
      print(matriz[i][j],end=" ")
  print()
soma=0
aux = ordem-1

for i in range(ordem):
  soma= soma + matriz[i][aux]
  aux= aux-1
print()
print("o resutado da soma dos elementos da diagonal secundaria é:",soma)