maior = menor = cont = soma_veiculos = soma_acidentes = soma_2k = 0
cid_maior = cid_menor = ''
for i in range(1,6):
    cidade  = str(input("\nDigite o nome da cidade : ", ))
    codigo = int(input("Digite o código da cidade: "))
    veiculos    = int(input("Numero de veiculos de passeio : "))
    acidentes   = int(input("Numero de acidentes de transito com vitimas: "))

    soma_veiculos += veiculos
    soma_acidentes += acidentes

    if acidentes > maior:
        maior = acidentes
        cid_maior = cidade

    if acidentes < menor or i == 1:
        menor = acidentes
        cid_menor = cidade

    if veiculos < 2000:
        soma_2k += acidentes
        cont += 1


media = soma_veiculos / i
media_2k = soma_2k / cont

print("O menor indice de acidentes de transito :", menor, "\nCidade que esse indice pertence é:", cid_menor)
print("O maior indice de acidentes de transito é:", acidentes, "\nCidade que pertence:", cid_maior)
print("Média de veiculos nas cincos cidades:", media)
print(f"Media de acidentes de transitos nas cidades com menos de 2000 veiculos de passeio é:", media_2k) 