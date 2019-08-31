cont = 0

R1 = str(input("Telefonou para a vítima ? "))
R2 = str(input("Esteve no local do crime ? "))
R3 = str(input("Mora perto da vítima ? "))
R4 = str(input("Devia para a vítima ? "))
R5 = str(input("Já trabalhou com a vítima ? "))


if R1 == "sim":
    cont = cont + 1
else:
    cont = cont + 0
    

if R2 == "sim":
    cont = cont + 1
else:
    cont = cont + 0
    
    

if R3 == "sim":
    cont = cont + 1
else:
    cont = cont + 0

if R4 == "sim":
    cont = cont + 1
else:
    cont = cont + 0
    

if R5 == "sim":
    cont = cont + 1
else:
    cont = cont + 0
    


if cont == 2:
    print("Suspeito")
elif cont == 3 or cont == 4:
    print("Cúmplice")
elif cont == 5:
    print("Assassino")
else:
    print("Inocente")

    
