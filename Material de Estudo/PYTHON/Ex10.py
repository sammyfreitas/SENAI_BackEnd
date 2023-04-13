print('---------DIAS DA SEMANA---------')
print('--------------------------------')
print('''
        MENU:
        [1] - Domingo
		[2] - Segunda-Feira
		[3] - Terça-Feira
		[4] - Quarta-Feira
		[5] - Quinta-Feira
        [6] - Sexta=Feira
		[7] - Sábado
	''')
opcao = int(input('Escolha uma opção: '))
if (opcao ==1):
	print('O dia da semana escolhido foi Domingo')
elif (opcao ==2):
	print('O dia da semana escolhido foi Segunda-Feira')
elif (opcao ==3):
	print('O dia da semana escolhido foi Terça-Feira')
elif (opcao ==4):
	print('O dia da semana escolhido foi Quarta-Feira')
elif (opcao ==5):
	print('O dia da semana escolhido foi Quinta-Feira')
elif (opcao ==6):
	print('O dia da semana escolhido foi Sexta-Feira')
elif (opcao ==7):
	print('O dia da semana escolhido foi Sábado')
else:
	print('Opção inválida')