import random
import statistics
media = 0
maior = aux = 0
contP = 0
contN = 0
par=0
impar=0
menor = 100
lista=[]
for cont in range (0,50):
    aux=int(random.randint(-10,10))
    media += aux
    lista.append(aux)
    if (aux>0):
        contP += 1
    if (aux<0):
        contN += 1  
print('-------------------------------------------------------------------------------------------------')  
print('---------------------- GERANDO NÚMEROS RANDOMICAMENTE E CONTANDO OS TIPOS -----------------------')
print('-------------------------------------------------------------------------------------------------')   
print(f'.       A média                           é : {round((media/cont),2)}')
print(f'        A quantidade de números positivos é : {contP}')
print(f'        A quantidade de números negativos é : {contN}')
print('-------------------------------------------------------------------------------------------------') 
print(f'        A lista de números é: ')
print(lista)
print('-------------------------------------------------------------------------------------------------') 