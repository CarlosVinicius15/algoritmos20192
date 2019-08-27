turno = str(input ("Em que turno você estuda ?  Digite (M) para  Matutino ou Digite (V) para Vespertino ou Digite (N) para Noturno: ").upper())
if turno == "M":
    print ("Bom dia.")
elif turno == "V":
    print ("Boa tarde.")
elif turno == "N":
    print ("Boa noite.")      
else:
    print ("Valor inválido")      
