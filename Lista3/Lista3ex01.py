nota = int(input("Digite uma nota de 0 até 10: "))
while nota < 0 or nota > 10:
    print("Valor inválido")
    nota = int(input ("Tente novamente, digite uma nota de 0 até 10: "))
print("Valor válido")
