cont = 0
numero = 0
maior = 0
menor = 0
while cont < 10:
	numero = int(input("Digite um número: "))
	cont = cont + 1
	if numero > maior:
		maior = numero
print("O maior número é %d" %maior)
		