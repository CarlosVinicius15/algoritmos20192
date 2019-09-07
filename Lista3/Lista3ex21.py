num = int(input("Digite um número: "))

while n <= 1:
    print("\nO valor não pode ser menor ou igual à um, digite novamente.")
    n = int(input("Digite um número: "))

print("\nEntre 1 e",num,"são primos os números: ")


x = 2 

while x <= num - 1: 
    y = 0 
    z = 1

    while z < 100: 
        if x % z == 0:
            y += 1 
        z += 1 
    
    if y == 2: 
        print(x)
    
    x += 1