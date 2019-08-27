n1 = int (input ("Digite o primeiro número: "))
n2 = int (input ("Digite o segundo número: "))
n3 = int (input ("Digite o terceiro número: "))

if n1 > n2 and n2 > n3:
    print ("Do maior para o menor:", n1, n2, n3)
if n1 > n3 and n3 > n2:
    print ("Do maior para o menor:", n1, n3, n2)
if n2 > n1 and n1 > n3:
    print ("Do maior para o menor:", n2, n1, n3)
if n2 > n3 and n3 > n1:
    print ("Do maior para o menor:", n2, n3, n1)
if n3 > n2 and n2 > n1:
    print ("Do maior para o menor:", n3, n2, n1)
if n3 > n1 and n1 > n2: 
    print ("Do maior para o menor:", n3 , n1, n2)