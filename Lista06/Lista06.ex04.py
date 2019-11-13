matriz = []
for i in range(10):
    matriz.append([0]*10)
for i in range(10):
    for j in range(10):
        matriz[i][j] = int(input("A[" + str(i+1) + "][" + str(j+1) + "]: "))
for i in range(10):
    for j in range(10):
        if i < j:
           matriz[i][j] = 2*i + 7*j - 2    
        elif i == j:
           matriz[i][j] = 3*(i**2) - 1
        else:
           matriz[i][j] = 4*(i**3) - 5*(j**2) + 1     
for i in range(10):
    for j in range(10):
         print([matriz[i][j]],end = " ")
    print()