import random
import statistics
media = 0
maior = aux = 0
contP = 0
contN = 0
par=0
impar=0
menor = 100
zero=0
lista=[]
for cont in range (0,255):
    aux=int(random.randint(10,100))
    lista.append(aux)
    
    resto= abs(aux)%2
    if (resto==0):
        par += 1
    else:
        impar += 1
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
print(f'        A quantidade de zeros             é : {(50-(contP+contN))}')
print('-------------------------------------------------------------------------------------------------') 
print(f'        A quantidade de números pares     é : {par}')
print(f'        A quantidade de números ímpares   é : {impar}')
print(f'        A lista de números é: ')
print(lista)
print('-------------------------------------------------------------------------------------------------') 