divida = float(input("Digite o valor da divida: "))
parcela = 1
print("\n" * 2)
print("Valor da divida: ", end="  ")
print("Valor do juros: ", end="  ")
print("Quantidade de parcelas: ", end="  ")
print("Valor da parcela: ")
for i in range(5):
    if parcela == 1:
    	juros = 1
    	valor_juros = 0
    elif parcela == 4:
        parcela = 3
        juros = 1.10
    elif parcela == 7 or parcela == 6:
        parcela = 6
        juros = 1.15
    elif parcela == 10 or parcela == 9:
        parcela = 9
        juros = 1.20
    elif parcela == 13 or parcela == 12:
        parcela = 12
        juros = 1.25

    valor_juros = divida * (juros - 1)
    divida_com_juros = divida * juros
    valor_parcela = divida_com_juros / parcela

    print("R$ %.2f" %divida_com_juros, end="            ")
    print("%.2f"%valor_juros, end="                    ")
    print(parcela, end="                    ")
    print("R$ %.2f"%valor_parcela)
    parcela = parcela + 3