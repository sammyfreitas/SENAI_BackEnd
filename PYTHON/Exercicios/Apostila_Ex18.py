#18. Faça um algoritmo que leia os valores de COMPRIMENTO, LARGURA e ALTURA e apresente o valor do volume de uma caixa retangular. 
#Utilize para o cálculo a fórmula VOLUME = COMPRIMENTO * LARGURA * ALTURA.
#
print('--------------------------------------------------------------------------')
print('------------------CÁLCULO DE VOLUME DE CAIXA RETANGULAR-------------------')
print('--------------------------------------------------------------------------')
comprimento = float(input('Informe o comprimento da caixa retangular (em cm): '))
altura = float(input('Informe a altura da caixa retangular      (em cm): '))
largura = float(input('Informe a largura da caixa retangular     (em cm): '))
volume=round((comprimento*altura*largura),2)
print('--------------------------------------------------------------------------')
print(f'As medidas da caixa são: Altura: {altura}, Comprimento: {comprimento} e Largura {largura}')
print(f'O volme da caixa retangular é  : {volume} cm³')
print('--------------------------------------------------------------------------')