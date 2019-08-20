
valor_original = float(input ("Informe o valor original da dívida: "))
atraso = int(input ("Informe a quantidade de dias em atraso: "))
multa = float(input("Informe o valor da dívida por dias em atraso: "))
taxa_extra = atraso * multa
divida_atrasada = taxa_extra + valor_original
print ("A taxa extra pelo atraso será de {} R$".format(taxa_extra) )
print ("O valor total a ser pago pela dívida em atraso será de {} R$".format (divida_atrasada))
