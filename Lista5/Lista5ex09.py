numero = []
par = []
impar = []
quant = int (input("Quantos números quer digitar ? "))
for i in range (1,quant + 1):
    
    valor = int ( input ( "Digite um número: " ) )
    
    numero.append ( valor )
    
    if ( valor % 2 ) == 0:
        par.append ( valor )
    else:
        impar.append ( valor )

print ("Vetor completo: ", numero )
print ("Vetor com números pares:", par )
print ("Vetor com números impares: ", impar )
