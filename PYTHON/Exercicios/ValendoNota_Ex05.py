import random

maior = aux = cont = qtde = 0
lista=[]


while cont < 101:
    cont+-1
    aux=int(random.randint(0,500))
    lista.append(aux)  

print('-------------------------------------------------------------------------------------------------')  
print('------- GERANDO NÚMEROS RANDOMICAMENTE E ORDENANDO A LISTA ----------')
print('-------------------------------------------------------------------------------------------------')   
print('Os números em ordem crescente são ',sorted(lista))
print('Os números em ordem decrescente são ',sorted(lista, reverse=True))
print('-------------------------------------------------------------------------------------------------') 