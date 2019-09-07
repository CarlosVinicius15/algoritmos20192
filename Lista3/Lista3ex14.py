Quantidade=int(input("Informe a quantidade de números que deseja observar: " ))
valor = int(input("Digite um número: "))
maior = valor
menor = valor
soma = valor
contador = 0
while contador< Quantidade-1:
    valor = int(input("Digite um número: "))
    soma=valor + soma
    contador=contador+1
    if valor > maior:
        maior=valor
    elif valor < menor:
        menor=valor        
print("o menor valor é: ",menor)
print("o maior valor é: ",maior)
print("soma =",soma)