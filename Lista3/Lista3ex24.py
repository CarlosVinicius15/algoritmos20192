continua = 'S'
totalAlunos = 0
somaAcertos = 0

while (continua.upper() == 'S'):
    acertos = 0
    print ('Informe a resposta de cada questao:')
    resposta = input('Questao 1: ')
    if (resposta == 'A'):
        acertos += 1
    resposta = input('Questao 2: ')
    if (resposta == 'B'):
        acertos += 1
    resposta = input('Questao 3: ')
    if (resposta == 'C'):
        acertos += 1
    resposta = input('Questao 4: ')
    if (resposta == 'D'):
        acertos += 1
    resposta = input('Questao 5: ')
    if (resposta == 'E'):
        acertos += 1
    resposta = input('Questao 6: ')
    if (resposta == 'E'):
        acertos += 1
    resposta = input('Questao 7: ')
    if (resposta == 'D'):
        acertos += 1
    resposta = input('Questao 8: ')
    if (resposta == 'C'):
        acertos += 1
    resposta = input('Questao 9: ')
    if (resposta == 'B'):
        acertos += 1
    resposta = input('Questao 10: ')
    if (resposta == 'A'):
        acertos += 1

    somaAcertos += acertos
    print ('Total de Acertos: %d' % acertos)

    if ('maiorAcerto' not in vars()) or (acertos > maiorAcerto):
        maiorAcerto = acertos
    if ('menorAcerto' not in vars()) or (acertos < menorAcerto):
        menorAcerto = acertos

    totalAlunos += 1

    continua = input('Deseja continuar (S/N): ')

print ('Maior acerto: %d' % maiorAcerto)
print ('Menor acerto: %d' % menorAcerto)
print ('Total de alunos que utilizaram o sistema: %d' % totalAlunos)
print ('Media de acertos: %.2f' % (somaAcertos / float(totalAlunos)))