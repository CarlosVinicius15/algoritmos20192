quantCD = int(input("Digite a quantidade de CDs: "))
valorTotal = 0
for i in range(quantCD):
	valorCD = float(input("Digite o valor do CD: "))
	valorTotal = valorTotal + valorCD
	valorMedio = valorTotal / quantCD
print("O valor total gasto foi de: R$", valorTotal)
print("O valor médio gasto por cada CD foi de: R$ %.2f" % valorMedio)
