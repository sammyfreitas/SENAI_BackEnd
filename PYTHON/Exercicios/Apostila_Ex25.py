#25. Faça um algoritmo que leia dois números inteiros (Int1 e Int2) e 
# imprima o quociente e o resto da divisão inteira de Int1 por Int2. 

int1 = int(input('Informe o 1º número : '))
int2 = int(input('Informe o 1º número : '))
quoc  = int(int1/int2)
resto = int1%int2
print('---------------------------------------------------')
print(f'Os números são            : [{int1}] e [{int2}]')
print(f'O quociente da divisão é  : {quoc}')
print(f'O resto da divisão é      : {resto}')
print('---------------------------------------------------')