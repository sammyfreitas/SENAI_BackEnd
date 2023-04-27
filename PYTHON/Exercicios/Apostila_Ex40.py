#40. Uma empresa produz três tipos de peças mecânicas: parafusos, porcas e arruelas. 
#Têm-se os preços unitários de cada tipo de peça e sabe-se que sobre estes preços incidem descontos de 
#10% para porcas, 
#20% para parafusos e 
#30% para arruelas. 
#Escreva um algoritmo que calcule o valor total da compra de um cliente. 
#Deve ser mostrado o nome do cliente. 
#O número de cada tipo de peça que o mesmo comprou, 
#o total de desconto e 
#o total a pagar pela compra. 
vlparafuso = 1.3
vlporca = 0.8
vlarruela = 0.5
print('----------------------------------------------------------------------')
nome_cliente=str(input('Digite o nome do cliente                  : '))
parafusos=int(input('Digite a quantidade de parafusos comprados: '))
porcas=int(input('Digite a quantidade de porcas compradas   : '))
arruelas=int(input('Digite a quantidade de arruelas compradas : '))

vltot_paraf=round((parafusos*vlparafuso),2)
vltot_porca=round((porcas*vlporca),2)
vltot_arruela=round((arruelas*vlarruela),2)

desc_paraf=round((vltot_paraf*0.2),2)
desc_porca=round((vltot_porca*0.1),2)
desc_arruela=round((vltot_arruela*0.3),2)

desc_total=desc_paraf+desc_porca+desc_arruela
venda=round((vltot_arruela+vltot_paraf+vltot_porca),2)
venda_desc=round((venda-desc_total),2)
print('''

    ''')
print('----------------- VENDA DE PEÇAS MECÂNICAS ---------------------------')
print(f'CLIENTE : {nome_cliente}')
print('----------------------------------------------------------------------')
print(f'PARAFUSOS : {parafusos}      VALOR TOTAL R$ {vltot_paraf}   DESCONTO R$ {desc_paraf}')
print(f'PORCAS    : {porcas}      VALOR TOTAL R$ {vltot_porca}    DESCONTO R$ {desc_porca}')
print(f'ARRUELAS  : {arruelas}      VALOR TOTAL R$ {vltot_arruela}    DESCONTO R$ {desc_arruela}')
print('----------------------------------------------------------------------')
print(f'VALOR TOTAL VENDA  : R$ {venda}               DESCONTO R$ {desc_total}') 
print('----------------------------------------------------------------------')
print(f'VALOR A PAGAR      : R$ {venda_desc}')  
print('----------------------------------------------------------------------')