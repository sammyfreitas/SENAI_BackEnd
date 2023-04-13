print('---------CALCULADORA---------')
var1 = float(input('Insira o primeiro número: '))
var2 = float(input('Insira o segundo número:  '))
print('-----------------------------')
print('''
        MENU:
        [1] - Adição
		[2] - Subtração
		[3] - Multiplicação
		[4] - Divisão
	''')
opcao = int(input('Escolha uma opção: '))
if (opcao ==1):
	calculo=round(var1+var2,2)
	print(f'A soma entre {var1} e {var2} é {calculo}')
elif (opcao ==2):
	calculo=round(var1-var2,2)
	print(f'A diferença entre {var1} e {var2} é {calculo}')
elif (opcao ==3):
	calculo=round(var1*var2,2)
	print(f'A multiplicação entre {var1} e {var2} é {calculo}')
elif (opcao ==4):
	calculo=round(var1/var2,2)
	print(f'A divisão entre {var1} e {var2} é {calculo}')
else:
	print('Opção inválida')