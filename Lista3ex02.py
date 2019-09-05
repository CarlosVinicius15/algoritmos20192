usuario = str(input ("Informe o nome de usuário: "))
senha = str(input ("Informe a senha: "))
while senha == usuario:
    print("Erro")
    usuario = str(input ("Informe o nome de usuário: "))
    senha = str(input ("Informe uma senha diferente do nome de usuário: "))
print ("Usuário: %s | Senha: %s" %(usuario, senha))

