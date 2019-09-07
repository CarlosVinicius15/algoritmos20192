num = int(input("Digite o valor do número que deseja calcular o fatorial: "))
fat = 1
i = 2
while i <= num:
	fat = i * fat
	i = i + 1

print("O valor de %d! é ="%num, fat)