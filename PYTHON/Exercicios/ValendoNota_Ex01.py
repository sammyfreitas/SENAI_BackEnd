"""
#1 -. A revendedora de carrosLtda. paga aos seus funcionários vendedores dois salários mínimos fixos, mais uma comissão fixa de R$ 50,00 por carro vendido e mais 5% do valor das vendas. Faça um algoritmo que determine o salário total de um vendedor.
"""

sal_minimo = 1302
com_fixa = 50
com_variavel=0.05
print('----------------------------------------------------------------------')
vendedor=str(input('Digite o nome do vendedor             : '))
carros_vendidos=int(input('Digite a quantidade de carros vendidos: '))
total_vendas=int(input('Digite o valor vendido                : '))
comissao=(com_fixa*carros_vendidos)+(total_vendas*com_variavel)
salario=round(((sal_minimo*2)+comissao),2)

print('----------------- REVENDEDORA DE LTDA  ---------------------------')
print(f'VENDEDOR : {vendedor}')
print('----------------------------------------------------------------------')
print(f'CARROS VENDIDOS    : {carros_vendidos}')
print(f'VALOR TOTAL VENDIDO: R$ {total_vendas}')
print(f'COMISSÃO           : R$ {comissao}')
print('----------------------------------------------------------------------')
print(f'SALARIO TOTAL      : R$ {salario}') 
print('----------------------------------------------------------------------')