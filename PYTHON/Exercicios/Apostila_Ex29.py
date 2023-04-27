#29. Admitindo que uma data é lida pelo algoritmo em uma variável inteira, e não em uma variável do tipo data, 
#crie um algoritmo que leia uma data no formato DDMMAA e imprima essa data no formato AAMMDD, onde:
#• A letra D corresponde a dois algarismos representando o dia;
#• A letra M corresponde a dois algarismos representando o mês;
#• A letra A corresponde aos dois últimos algarismos representando o ano
#
data_lida = str(input('Informe a data no formato DDMMAA: '))
DD = N[0]+N[1]
MM = N[2]+N[3]
AA = N[4]+N[5]
nova_data = str(AA+DD+MM)
print('---------------------------------------------------')
print(f'A data no formato DDMMAA é : {data_lida}')
print(f'A data no formato AAMMDD é : {nova_data}')
print('---------------------------------------------------')