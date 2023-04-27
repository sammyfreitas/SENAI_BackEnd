print('''
        MENU:
        [1] - Venda a vista
		[2] - Venda a Prazo com 30 dias
		[3] - Venda a Prazo com 60 dias
		[4] - Venda a Prazo com 90 dias
		[5] - Venda com cartão de débito
		[6] - Venda com cartão de crédito
	''')
opcao = int(input('Escolha uma opção: '))

if (opcao ==1):
	print('A opção escolhida foi VENDA À VISTA')
elif (opcao ==2):
	print('A opção escolhida foi VENDA A PRAZO COM 30 DIAS')
elif (opcao ==3):
	print('A opção escolhida foi VENDA A PRAZO COM 60 DIAS')
elif (opcao ==4):
	print('A opção escolhida foi VENDA A PRAZO COM 90 DIAS')
elif (opcao ==5):
	print('A opção escolhida foi VENDA COM CARTÃO DE DÉBITO')
elif (opcao ==6):
	print('A opção escolhida foi VENDA COM CARTÃO DE CRÉDITO')
else:
	print('Opção inválida')
	