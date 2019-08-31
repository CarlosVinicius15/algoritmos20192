Csala = float(input ("Informe o valor do comprimento da sala: "))
Lsala = float(input ("Informe o valor da largura da sala: "))
C_carteira = float(input ("Informe o valor do comprimento da carteira: "))
L_carteira = float(input ("Informe o valor da largura da carteira: "))
total_l = int((Lsala + 0.5) / (L_carteira + 0.5))
total_c = int((Csala - 1.5 + 0.2) / (C_carteira + 0.2))
Total_sala = total_l * total_c
print ("O total de carteiras na sala é ", Total_sala)
