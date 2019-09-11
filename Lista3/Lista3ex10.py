base=int(input("Base: "))
expoente=int(input("Expoente: "))

potencia=1

for cont in range(expoente):
    potencia = potencia * base
    cont =  cont + 1

print(base, "^", expoente, "=", potencia)