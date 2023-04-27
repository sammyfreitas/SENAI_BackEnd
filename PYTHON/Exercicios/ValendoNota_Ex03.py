"""
Faça um algoritmo que leia dois números e indique se são iguais ou se são 
diferentes. Mostre o maior e o menor (nesta sequência). 
"""

A = float(input('Informe o 1º número: '))
B = float(input('Informe o 2º número: '))
print('---------------------------------------------------')
print(f'Os números digitados foram : [{A}] e [{B}]')
if (A>B):
    print(f'O maior número é           : {A}')
elif (B>A):
    print(f'O maior número é           : {B}')
else:
    print('Os números são iguais')    
print('---------------------------------------------------')