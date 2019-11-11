numero = []
par = []
impar = []
quant = int (input("Quantos números quer digitar ? "))
for i in range (1,quant + 1):
    
    valor = int ( input ( "Digite um número: " ) )
    
    numero.append ( valor )  #Não é permitido a utilização de funções de listas
    
    if ( valor % 2 ) == 0:
        par.append ( valor )  #Não é permitido a utilização de funções de listas
    else:
        impar.append ( valor )  #Não é permitido a utilização de funções de listas

print ("Vetor completo: ", numero )
print ("Vetor com números pares:", par )
print ("Vetor com números impares: ", impar )
