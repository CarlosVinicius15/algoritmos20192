def criar_vetor ():
    n = int(input("Digite o tamanho do vetor: "))
         
    vetor = []
    for i in range(n):
         vetor.append(int(input("Informe um valor para o vetor: ")))

    return vetor
    
def crescente (vetor,tamanho):
	verificar = True
	
	for i in range(tamanho - 1):
		if vetor[i] > vetor[i + 1]:
			verificar = False
	if verificar:
		print("\nO vetor está em ordem crescente.")
	else:
		print("\nO vetor não esta em ordem crescente.")
              
vetor = criar_vetor()

crescente (vetor,len(vetor))