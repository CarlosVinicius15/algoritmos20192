def criar_vetor ():
    n = int(input("Digite o tamanho do vetor:"))
         
    vetor = []
    for i in range(n):
         lista.append(int(input("informe um elemento para o vetor: ")))

    return lista
    
def crescente (vetor,tamanho):
    verificar = True

    for i in range(tamanho - 1):
        if vetor[i] > vetor[i +1]:
            verificar = False

    if verificar:
        print("\nO vetor está em ordem crescente.")
    else:
        print("\nO vetor não está em ordem crescente.")
              
lista = criar_vetor()

crescente (vetor,len(vetor))
print(vetor)
