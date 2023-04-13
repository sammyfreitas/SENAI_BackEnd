#26. Considere a seguinte situação: 
#descontam-se inicialmente 10% do salário bruto do trabalhador como contribuição à previdência social.
#Após esse desconto, há um outro desconto de 5% sobre o valor restante do salário bruto, a título de um determinado imposto. 
#Faça um algoritmo que leia o salário bruto de um cidadão e imprima o seu salário líquido. 

salbruto = float(input('Informe o salário bruto: '))
prevsocial = round((salbruto*0.1),2)
salprev=round((salbruto-prevsocial),2)
imposto=round((salprev*0.05),2)
sal_liq=round((salprev-imposto),2)
print('---------------------------------------------------')
print(f'O salário bruto é               : R$ {salbruto}')
print(f'O valor da previdência social é : R$ {prevsocial}')
print(f'O imposto é                     : R$ {imposto}')
print(f'O salário líquido é             : R$ {sal_liq}')
print('---------------------------------------------------')