#15. Faça um algoritmo que calcule a quantidade de litros de combustível gasta em uma viagem, 
#utilizando um automóvel que faz 12Km por litro. 
#Para obter o cálculo, o usuário deve fornecer o tempo gasto na viagem e a velocidade média durante ela. 
#Desta forma, será possível obter a distância percorrida com a fórmula DISTANCIA = TEMPO * VELOCIDADE. 
#Tendo o valor da distância, basta calcular a quantidade de litros de combustível utilizada na viagem com a fórmula: LITROS_USADOS = DISTANCIA / 12. 
#O programa deve apresentar os valores da velocidade média, tempo gasto na viagem, a distância percorrida e a quantidade de litros utilizada na viagem. 
#
#
print('---------------------------------------------------')
print('----------------CALCULO COMBUSTIVEL----------------')
print('---------------------------------------------------')
tempo = float(input('Informe o tempo gasto na viagem (em horas)    : '))
veloc_media = float(input('Informe a velocidade média na viagem (em km)  : '))
distancia = round((tempo*veloc_media),2)
litros_usados = round((distancia/12),2)
print('---------------------------------------------------')
print(f'Tempo de Viagem                     : {tempo} h')
print(f'Velocidade Média                    : {veloc_media} km/h')
print(f'Distância Percorrida                : {distancia} km')
print(f'Quantidade de Litros de Combustível : {litros_usados} l')
print('---------------------------------------------------')