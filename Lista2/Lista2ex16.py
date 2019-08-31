morangokg = 2.50
macaskg = 1.80
QuantosMorangos = float(input("Quantos kg's de Morango quer comprar ? "))
QuantasMacas = float(input("Quantos kg's de Maçã quer comprar ? "))
if QuantosMorangos > 5:
    morangokg = 2.20
if QuantasMacas > 5:
    macaskg = 1.50
ValorTotal = (morangokg * QuantosMorangos) + (macaskg * QuantasMacas)
if (QuantosMorangos + QuantasMacas) > 8 or ValorTotal > 25.00:
    desconto = (ValorTotal * 10) / 100
    ValorTotal = ValorTotal - desconto
    print("O seu valor total foi... %.2f" % ValorTotal, "R$")
else:
    print("O seu valor total foi... %.2f" % ValorTotal, "R$")