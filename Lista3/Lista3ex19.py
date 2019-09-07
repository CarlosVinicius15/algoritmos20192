x = 1
valor = 1.99

print("\nLojas Quase Dois - Tabelas de preços\n")

while x <= 50:
    print("%02.d - R$ %.2f"%(x,x*valor))
    x = x + 1