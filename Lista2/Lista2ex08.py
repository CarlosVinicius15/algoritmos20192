vh = float(input("informe o valor que você recebe por hora: R$"))
qm = float(input("informe a quantidade de horas trabalhadas por mês:"))
sb = vh*qm
sb = float(sb)
IR = sb*5/100
IR = float(IR)
INSS = sb*10/100
INSS = float(INSS)
IR = float(IR)
FGTS = sb*11/100
FGTS = float(FGTS)

if sb <= 900 :
    print ("Salário bruto: R$", vh*qm)
elif sb > 900 and sb <= 1500 :
    print ("Salário Bruto: R$", sb)
    print ("IR (5%): R$", sb*5/100)
    print ("INSS (10%): R$", sb*10/100)
    print ("FGTS (11%): R$", sb*11/100)
    print ("Total de descontos: R$", IR+INSS)
    print ("Salário Liquido: R$", sb-(IR+INSS))

IR = sb*10/100
IR = float(IR)

if sb > 1500 and sb <= 2500 :
    print ("Salário Bruto: R$", sb)
    print ("IR (10%): R$", sb*10/100)
    print ("INSS (10%): R$", sb*10/100)
    print ("FGTS (11%): R$", sb*11/100)
    print ("Total de descontos: R$", IR+INSS)
    print ("Salário Liquido: R$", sb-(IR+INSS))

IR = sb*20/100
IR = float(IR)

if sb > 2500 :
    print ("Salário Bruto: R$", sb)
    print ("IR (20%): R$", sb*20/100)
    print ("INSS (10%): R$", sb*10/100)
    print ("FGTS (11%): R$", sb*11/100)
    print ("Total de descontos: R$", IR+INSS)
    print ("Salário Liquido: R$", sb-(IR+INSS))



    



        
 
