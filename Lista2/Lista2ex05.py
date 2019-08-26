produto1 = input("Digite o 1° preço: ")
produto2 = input("Digite o 2° preço: ")
produto3 = input("Digite o 3° preço: ")


if produto1 < produto2 and produto1 < produto3 :
    print ("O produto 1 é o mais barato.")
elif produto2 < produto1 and produto2 < produto3 :
    print ("O produto 2 é o mais barato.")
elif produto3 < produto1 and produto3 < produto2 :
    print ("O produto 3 é o mais barato.")

    

elif produto1 == produto2 and produto1 and produto2 < produto3 :
    print ("O produto 1 e 2 são os mais baratos.")
elif produto1 == produto3 and produto1 and produto3 < produto2 :
    print ("O produto 1 e 3 são os mais baratos.")
elif produto2 == produto3 and produto2 and produto3 < produto1 :
    print ("O produto 1 e 2 são os mais baratos.")

    

else:
    print ("Todos os preços são iguais.")


       

