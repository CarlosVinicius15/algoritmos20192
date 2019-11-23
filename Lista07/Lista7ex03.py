def criar_lista ():
    n = int(input("tamanho da lista:"))
    lista = []
    for i in range(n):
        lista.append(int(input("elemento da lista:")))

    return lista
    
def inverter_lista (lista,tamanho):
        print(lista[tamanho::-1])

lista = criar_lista()
inverter_lista(lista,len(lista))
