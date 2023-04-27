#19. Faça um algoritmo que leia um valor inteiro e 
#apresente os resultados do quadrado e do cubo do valor lido. 

print('--------------------------------------------------------------------------')
print('-----------------------QUADRADO E CUBO DE UM VALOR------------------------')
print('--------------------------------------------------------------------------')
num = float(input('Informe o número: '))
quadrado = round((num*num),2)
cubo = round((num*num*num),2)
print('--------------------------------------------------------------------------')
print(f'O número é             : {num}')
print(f'O quadrado do número é : {quadrado}')
print(f'O cubo do número é     : {cubo}')
print('--------------------------------------------------------------------------')