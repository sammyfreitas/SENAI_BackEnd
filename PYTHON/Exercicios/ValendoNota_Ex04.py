"""4- Um vendedor necessita de um algoritmo que calcule o preço total devido por um 
cliente. O algoritmo deve receber o código de um produto e a quantidade 
comprada e calcular o preço total, usando a tabela abaixo: 
Código do produto Preço unitário
 1001 			5,32 
 1324 			6,45 
 6548 			2,37 
 0987			5,32 
 7623 			6,45 
 """


print('--------------------------------------------------------------')
print('''
        MENU:
        [1] - Produto 1001
		[2] - Produto 1324
		[3] - Produto 6548
		[4] - Produto 0987
		[5] - Produto 7623
	''')
opcao = int(input('Escolha uma opção: '))
print('----------------------------------------------------------------------')

if (opcao == 1):
	qtde=int(input('Digite a quantidade comprada: \n'))
	valorunit=5.32
	valor=round((valorunit*qtde),2)
elif (opcao == 2):
	qtde=int(input('Digite a quantidade comprada: \n'))
	valorunit=6.45
	valor=round((valorunit*qtde),2)	
elif (opcao == 3):
	qtde=int(input('Digite a quantidade comprada: \n'))
	valorunit=2.37
	valor=round((valorunit*qtde),2)
elif (opcao == 4):
	qtde=int(input('Digite a quantidade comprada: \n'))
	valorunit=5.32
	valor=round((valorunit*qtde),2)
elif (opcao == 5):
	qtde=int(input('Digite a quantidade comprada: \n'))
	valorunit=6.45
	valor=round((valorunit*qtde),2)
else:
	print ("Opção Inválida")

print('----------------- VENDAS DO CLIENTE ---------------------------')
print(f'Produto       : {opcao} ')      
print(f'Total Vendido : {qtde}     	Valor Unitario R$ {valorunit} ')
print('----------------------------------------------------------------------')
print(f'VALOR TOTAL VENDA  : R$ {valor}               ') 
print('----------------------------------------------------------------------')
