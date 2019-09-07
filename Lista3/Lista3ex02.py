usuario = str(input("Nome de usuario: "))
senha = str(input("Senha: "))

while senha == usuario:
	print("Erro")
	usuario =str(input("Digite o nome de usuario novamente: "))
	senha = str(input("Digite uma senha diferente do nome de usuário: "))

print ("Usuário: %s | Senha: %s" %(usuario, senha))