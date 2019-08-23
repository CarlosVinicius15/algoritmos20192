salario = float(input ("Informe o salário mensal: "))
despesas = float( input ("Informe o total de despesas mensais: "))
sobra_mensal = salario - despesas
ganho_anual = sobra_mensal * 12
print ("A sobra mensal é de: ", sobra_mensal, "R$")
total_poupar = int(1000000 / ganho_anual)
print ("Com esses valores, uma pessoa irá juntar  R$ 1.000.000,00 em", total_poupar, "anos." )

