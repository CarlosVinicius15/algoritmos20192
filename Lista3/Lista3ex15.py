num = int(input("Digite um número inteiro: "))
primo = True
for i in range (2, num//2 + 1, 1):
	if num % i == 0:
		primo = False
if primo:
	print ("O número é primo.")
else:
	print ("O número não é primo.")