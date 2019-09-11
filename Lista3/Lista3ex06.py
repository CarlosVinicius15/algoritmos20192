num = 0
soma = 0
quant = 0
while quant < 10:
	num = int(input("Digite um número: "))
	soma += num
	quant += 1
	if quant > 10:
		media = soma / quant
		print (soma)
		print (media)