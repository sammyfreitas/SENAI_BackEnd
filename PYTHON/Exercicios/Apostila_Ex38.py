#38. Faça um algoritmo que leia os valores A, B e C. 
#Mostre uma mensagem que informe se a soma de A com B é menor, maior ou igual a C. 

A=float(input('Digite o 1º valor: '))
B=float(input('Digite o 2º valor: '))
C=float(input('Digite o 3º valor: '))

if ((A+B)>C):
    msg=('maior que ')
elif ((A+B)<C):
    msg=('menor que ')
else:
    msg=('igual a')


print('------------------------------------------------------------------------------------') 
print(f'Os valores digitados foram {A:.0f}, {B:.0f} e {C:.0f}')
print(f'A soma de [{A:.0f}] e [{B:.0f}] é {msg} [{C:.0f}]')
print('------------------------------------------------------------------------------------') 
