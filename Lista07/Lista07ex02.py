def ler_vetorStr(tam,vet):
    for i in range(tam):
        vet[i] = input("Digite a resposta "+ str(i+1) + ": ")

def acertos_erros(respostas,gabarito,tam):
    acertos = 0
    erros = 0
    for i in range(tam):
        if respostas[i] == gabarito[i]:
            acertos= float(acertos + 1)
        else:
            erros= float(erros + 1)
    acertos_erros = [acertos,erros]
    return acertos_erros

tamanho = int(input("Quantas questões teve na prova? "))
respostas = [""]*tamanho
gabarito = [""]*tamanho
ler_vetorStr(tamanho,respostas)
ler_vetorStr(tamanho,gabarito)
acertos_e_erros = acertos_erros(respostas,gabarito,tamanho)
percentual = (acertos_e_erros[0] * 100) / tamanho
print("Seu percentual de acertos foi de:",percentual, "% !")