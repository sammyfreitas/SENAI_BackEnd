#16. Faça um algoritmo que leia dois valores para as variáveis A e B e efetue a troca dos valores 
#de forma que a variável A passe a possuir o valor da variável B e a variável B passe a possuir o valor da variável A. 
#Apresente os valores trocados. 
#
print('--------------------------------------------------------------------------')
print('-------------------------TROCA VALORES VARIÁVEIS--------------------------')
print('--------------------------------------------------------------------------')
A = int(input('Informe o valor da variável A : '))
B = int(input('Informe o valor da variável B : '))
TROCA1 = A
TROCA2 = B
B=TROCA1
A=TROCA2
print('--------------------------------------------------------------------------')
print(f'O valor inicial da variável A era [{TROCA1}] e foi trocado para {A}')
print(f'O valor inicial da variável B era [{TROCA2}] e foi trocado para {B}')
print('--------------------------------------------------------------------------')