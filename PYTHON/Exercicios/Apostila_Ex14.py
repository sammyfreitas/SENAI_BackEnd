#14. Faça um algoritmo que calcule e apresente o valor do volume de uma lata de óleo, 
#utilizando a fórmula VOLUME = 3,14159 * RAIO2 * ALTURA. 
#
raio = float(input('Digite o Raio da Lata de Óleo: '))
altura = float(input('Digite a Altura da Lata de Óleo: '))
pi=3.14159
volume=round(((raio*raio)*altura*pi),2)
print(f'O Volume da Lata de Óleo é: {volume}')
