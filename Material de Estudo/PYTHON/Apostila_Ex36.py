#36. Uma empresa de vendas tem três corretores. A empresa paga ao corretor uma comissão calculada de acordo com o valor de suas vendas. 
#Se o valor da venda de um corretor for maior que R$ 50.000.00 a comissão será de 12% do valor vendido. 
#Se o valor da venda do corretor estiver entre R$ 30.000.00 e R$ 50.000.00 (incluindo extremos) a comissão será de 9.5%. 
#Em qualquer outro caso, a comissão será de 7%. 
#Escreva um algoritmo que gere um relatório contendo nome, valor da venda e comissão de cada um dos corretores. 
#O relatório deve mostrar também o total de vendas da empresa.


corretor1=str(input('Digite o nome do Corretor             : '))
venda1=float(input('Digite o valor das Vendas do Corretor : '))
print('--------------------------------------------------------------------------')
corretor2=str(input('Digite o nome do Corretor             : '))
venda2=float(input('Digite o valor das Vendas do Corretor : '))
print('--------------------------------------------------------------------------')
corretor3=str(input('Digite o nome do Corretor             : '))
venda3=float(input('Digite o valor das Vendas do Corretor : '))
print('--------------------------------------------------------------------------')

#calculo comissão vendedor 1
if (venda1<30000):
    comissao1=round((venda1*0.07),2)
elif ((venda1>=30000) and (venda1<=50000)):
    comissao1=round((venda1*0.095),2)
else:
    comissao1=round((venda1*0.12),2)

#calculo comissão vendedor 2
if (venda2<30000):
    comissao2=round((venda2*0.07),2)
elif ((venda2>=30000) and (venda2<=50000)):
    comissao2=round((venda2*0.095),2)
else:
    comissao2=round((venda2*0.12),2)
    
#calculo comissão vendedor 3
if (venda3<30000):
    comissao3=round((venda3*0.07),2)
elif ((venda3>=30000) and (venda3<=50000)):
    comissao3=round((venda3*0.095),2)
else:
    comissao3=round((venda3*0.12),2)


#calculo total vendas
total_vend = round((venda1+venda2+venda3),2)

#calculo lucro liquido
lucro_liq = round(((total_vend)-(comissao1+comissao2+comissao3)),2)

    
print('-------------------------------- VENDAS EMPRESA XYZ --------------------------------------')
print(f'Corretor: {corretor1}       Valor Vendas: R$ {venda1}      Comissão: R$ {comissao1}')
print(f'Corretor: {corretor2}       Valor Vendas: R$ {venda2}      Comissão: R$ {comissao2}')
print(f'Corretor: {corretor3}       Valor Vendas: R$ {venda3}      Comissão: R$ {comissao3}')
print('------------------------------------------------------------------------------------------')  
print(f'Total de Vendas                         : {total_vend}') 
print(f'Total de Lucro Líquido                  : {lucro_liq}') 
print('------------------------------------------------------------------------------------------')  
