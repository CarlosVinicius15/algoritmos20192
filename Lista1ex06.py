salario = float( input ("Informe o salário atual: "))
percentual= float( input ("Informe o percentual de reajuste: "))
reajuste = (percentual / 100) * salario 
novo_valor = reajuste + salario
print ("O novo valor do salário do funcionário será", novo_valor,"R$")

