def par (vetor,tamanho):
    print("\nValores pares: ")
    for j in range(tamanho):
       if(vetor[j] % 2) == 0 :
          print(vetor[j], end = " ")
    print()
          
def impar (lista,tamanho):
    print("\nValores impares: ")
    for k in range (tamanho):
        if (vetor[k]%2) != 0 :
            print(vetor[k],end = " ")
            
tamanho = int(input("Digite o tamanho do vetor: "))
vetor = []

for i in range (tamanho):
    vetor.append(int(input("digita o numero:")))

par(vetor,tamanho)
impar(vetor,tamanho)
