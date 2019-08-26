nota1 = float( input ("Informe a primeira nota parcial: "))
nota2 = float( input ("Informe a segunda nota parcial: "))
media = (nota1 + nota2) / 2
print ("A média do aluno foi", media)
if media >= 7 :
    print ("Aprovado")
elif media >= 5 and media < 7 :     
    print ("Prova final")
else:
    print ("Reprovado")
        