#21. Faça um algoritmo que leia dois valores inteiros (A e B) e 
#apresente o resultado da soma do quadrado de cada valor lido. 

print('--------------------------------------------------------------------------')
print('--------------------QUADRADO DA SOMA DE DOIS VALORES----------------------')
print('--------------------------------------------------------------------------')
num1 = int(input('Informe o 1º número: '))
num2 = int(input('Informe o 2º número: '))
quad1 = round((num1*num1),2)
quad2 = round((num2*num2),2)
soma = round((quad1+quad2),2)
print('--------------------------------------------------------------------------')
print(f'O primeiro número é              : {num1} e seu quadrado é : {quad1}')
print(f'O segundo número é               : {num2} e seu quadrado é : {quad2}')
print(f'A soma dos quadrados é           : {soma}')
print('--------------------------------------------------------------------------')