quantidade = 0
while (quantidade <= 0):
    quantidade = int(input('Informe a quantidade de pessoas: '))
    if (quantidade <= 0):
        print ("A quantidade deve ser positiva.")
soma = 0
for i in range(0, quantidade):
    idade = -1
    while (idade < 0):
        idade = int(input("Informe a idade da pessoa: "))
        if (idade < 0):
            print ("A idade não pode ser negativa.")
    soma += idade 

media = soma / float(quantidade)

if (media <= 25):
    print ("A turma é jovem")
elif (media <= 60):
    print ("A turma é adulta")
else:
    print ("A turma é idosa.")