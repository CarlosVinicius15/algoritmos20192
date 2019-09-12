while True:
    n = 1
    total = 0

    while True:
        preco = float(input("Produto {}: R$ ".format(n)))
        n += 1
        total += preco
        if preco == 0:
            break

    

    print("Total: R$ {:.2f} ".format(total))
    dinheiro = float(input("Dinheiro: R$ "))
    print("Troco: R$ {:.2f}".format(dinheiro - total))

   

    reiniciar = input("pressione 0 para reiniciar ou pressione 1 para encerrar: ")
    if reiniciar == "0":
    	continue
    else:
        print("Encerrando caixa...")
        break