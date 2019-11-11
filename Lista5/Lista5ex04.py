maior = 0
cont = 0
vet = []
for i in range (0,10):
	valor = int(input("Digite um valor: "))
	vet.append(valor)  #Não é permitido a utilização de funções de listas
for i in range (0,10):
	if vet[i] > maior:
		cont = cont + 1
		maior = vet[i]
print ("O maior elemento é: %d \nSua posição é: %d" %(maior, cont))
