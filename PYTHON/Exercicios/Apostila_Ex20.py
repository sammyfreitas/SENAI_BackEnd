#20. Faça um algoritmo que leia dois valores inteiros (A e B) e 
#apresente o resultado do quadrado da soma dos valores lidos. 

print('--------------------------------------------------------------------------')
print('--------------------QUADRADO DA SOMA DE DOIS VALORES----------------------')
print('--------------------------------------------------------------------------')
num1 = int(input('Informe o 1º número: '))
num2 = int(input('Informe o 2º número: '))
soma = num1+num2
quadrado = round((soma*soma),2)
print('--------------------------------------------------------------------------')
print(f'O primeiro número é              : {num1}')
print(f'O segundo número é               : {num2}')
print(f'O soma dos números é             : {soma}')
print(f'O quadrado da soma dos números é : {quadrado}')
print('--------------------------------------------------------------------------')