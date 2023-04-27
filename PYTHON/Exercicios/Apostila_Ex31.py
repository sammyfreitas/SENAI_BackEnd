#31. Faça um algoritmo que leia dois números A e B e imprima o maior deles. 

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