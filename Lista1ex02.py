km_inicial = float(input ("Informe o Km inicial: "))
km_final = float(input ("Informe o Km final: "))
litros_gastos = float(input ("Informe quantos litros foram gastos durante o percurso: "))
percurso = km_final - km_inicial
print("O percurso total foi de: {} km".format(percurso))
media = float(percurso / litros_gastos)
print ("A media de consumo de combustivel no percurso foi de {} km/l".format(media))