#42. Uma pessoa comprou quatro artigos em uma loja. 
#Para cada artigo, tem-se nome, preço e percentual de desconto. 
#Faça um algoritmo que imprima:
# nome, 
# preço  
# preço com desconto de cada artigo e 
# o total a pagar. 

camisa = 25,00
bermuda= 50,00
casaco = 100,00
meias = 5,00

desc1=0.01
desc2=0.015
desc3=0.018
desc4=0.02


print('----------------------------------------------------------------------')

print('----------------------------------------------------------------------')
vendedor=str(input('Digite o nome do vendedor             : '))
carros_vendidos=int(input('Digite a quantidade de carros vendidos: '))
total_vendas=int(input('Digite o valor vendido                : '))
comissao=(com_fixa*carros_vendidos)+(total_vendas*com_variavel)
salario=round(((sal_minimo*2)+comissao),2)

print('----------------- REVENDEDORA DE CARROS PICA-PAU ---------------------------')
print(f'VENDEDOR : {vendedor}')
print('----------------------------------------------------------------------')
print(f'CARROS VENDIDOS    : {carros_vendidos}')
print(f'VALOR TOTAL VENDIDO: R$ {total_vendas}')
print(f'COMISSÃO           : R$ {comissao}')
print('----------------------------------------------------------------------')
print(f'SALARIO TOTAL      : R$ {salario}') 
print('----------------------------------------------------------------------')