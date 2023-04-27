print('---------ORGANIZANDO NÚMEROS---------')
A = int(input('Digite o 1º número: '))
B = int(input('Digite o 2º número: '))
C = int(input('Digite o 3º número: '))
print('--------------------------------')
print('''
        MENU:
        [1] - Ordem Crescente
		[2] - Ordem Decrescente
		[3] - Maior valor entre os números
	''')
opcao = int(input('Escolha uma opção: '))
print('--------------------------------')
lista=[A,B,C]
if (opcao ==1):
	print('Os números em ordem crescente são ',sorted(lista))
elif (opcao ==2):
	print('Os números em ordem decrescente são ',sorted(lista, reverse=True))
elif (opcao ==3):
    #Escolhendo o maior número para ficar no meio
    if A > B and A > C:
        print(f'Com o maior número no meio, a ordem fica: {B}, {A}, {C}')
    if B > A and B > C:
        print(f'Com o maior número no meio, a ordem fica: {A}, {B}, {C}')
    if C > A and C > B:
        print(f'Com o maior número no meio, a ordem fica: {A}, {C}, {B}')
else:
	print('Opção inválida')