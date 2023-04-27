#34. Construa um algoritmo que receba como entrada três valores e os imprima em ordem crescente.  
v1 = int(input('Informe o 1º número: '))
v2 = int(input('Informe o 2º número: '))
v3 = int(input('Informe o 3º número:'))
lista=[v1,v2,v3]
print('---------------------------------------------------')
print(f'Os números digitados foram       : {v1},  {v2} e {v3}')
print(f'Os números em ordem crescente são: ',sorted(lista))
print('---------------------------------------------------')