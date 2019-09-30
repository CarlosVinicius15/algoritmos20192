ch = input("Caractere: ")
for linha in range(12):
	for coluna in range(24):
		     if (linha + coluna) % 2 == 0:
		     	print(ch, ch,sep = ' ',end = ' ')
		     else:
		     	print('',sep ='',end ='')
	print()