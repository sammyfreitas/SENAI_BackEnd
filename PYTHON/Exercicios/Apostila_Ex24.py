#24. Faça um algoritmo que leia a velocidade de um veículo em km/h 
#e calcule e imprima a velocidade em m/s (metros por segundo).

print('---------------------------------------------------')
print('------------------ km/h PARA m/s ------------------')
print('---------------------------------------------------')
veloc_media = float(input('Informe a velocidade (em km/h)  : '))
m_seg  = round((veloc_media/3.6),2)
print('---------------------------------------------------')
print(f'Velocidade em Km/h          : {veloc_media} km/h')
print(f'Velocidade em  M/s          : {m_seg}  m/s')
print('---------------------------------------------------')