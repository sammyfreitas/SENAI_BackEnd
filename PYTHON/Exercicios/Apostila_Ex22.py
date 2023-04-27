#22. Faça um algoritmo que leia dois números nas variáveis Val1 e Val2, 
#calcule sua média na variável Media e imprima seu valor

print('-----------------------------------------------------')
print('-------------------- M É D I A ----------------------')
print('-----------------------------------------------------')
Val1 = float(input('Informe o 1º número: '))
Val2 = float(input('Informe o 2º número: '))
media = round(((Val1+Val2)/2),2)
print('-----------------------------------------------------')
print(f'O primeiro número é              : {Val1} ')
print(f'O segundo número é               : {Val2} ')
print(f'A média dos números é            : {media}')
print('-----------------------------------------------------')