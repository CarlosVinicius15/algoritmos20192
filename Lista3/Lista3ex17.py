qnt = int(input("Quantas turmas serão registradas: "))

while qnt < 1:
    print("\nRegistre ao menos uma turma.")
    qnt = int(input("Quantas turmas serão registradas: "))

cont = 0
soma = 0

while cont < qnt:
    t = int(input("\nTurma [ {} ]\nDigite quantos alunos tem nessa turma: ".format(cont+1)))

    while t < 0 or t > 40:
        if t < 0:
            print("\nDigite um valor maior ou igual à 0.")
        elif t > 40:
            print("\nUma turma não pode ter mais do que 40 alunos.")
        print("Digite novamente.")

        t = int(input("\nTurma [ {} ]\nDigite quantos alunos tem nessa turma: ".format(cont+1)))
    
    soma += t
    cont += 1

print("\nNúmero de turmas:",qnt)
print("Total de alunos:",soma)
print("\nMédia de alunos: %.2f"%(soma/qnt))