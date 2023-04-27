#37. Escreva um algoritmo que determine o número de dias que uma pessoa já viveu.
#Considere que um mês tenha 30 dias. 
from datetime import date
from datetime import datetime

nome=str(input('Digite o nome                           : '))
str_data=str(input('Digite a data de nascimento (DD/MM/AAAA): '))

#convertendo a data de nascimento digitada em data
datanasc = datetime.strptime(str_data, '%d/%m/%Y').date() 

#capturando a data do sistema
hoje = date.today()

#calculando a quantidade de dias
totdias=((hoje - datanasc).days)
totmeses=(totdias//30)
totanos=(totdias//365)
#calculando o tempo vivido 
dias=(hoje-datanasc).days
anos, dias = dias // 365, dias % 365
meses, dias = dias // 30, dias % 30

print('-------------------------------- DIAS VIVIDOS --------------------------------------')
print(f'NOME: {nome}               Data de Nascimento: {datanasc}')
print(f'Desde seu nascimento em {datanasc} passaram {anos} anos, {meses} meses, {dias} dias, {horas} horas') 
print('------------------------------------------------------------------------------------') 
print(f'Idade Total: ')
print(f'EM ANOS {totanos}           EM MESES: {totmeses}           EM DIAS : {totdias} ')
print('------------------------------------------------------------------------------------') 