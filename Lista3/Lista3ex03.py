populaçãoA=80000
populaçãoB=200000
ano=0
while populaçãoA < populaçãoB:
	populaçãoA = populaçãoA + int((populaçãoA*3.0)/100)
	populaçãoB = populaçãoB + int((populaçãoB*1.5)/100)
	ano = ano + 1

print("levará",ano,"anos para população da cidade A ser maior que a cidade B")
print("populaçãoB-->",populaçãoB,"habitantes")
print("populaçãoA-->", populaçãoA,"habitantes")
