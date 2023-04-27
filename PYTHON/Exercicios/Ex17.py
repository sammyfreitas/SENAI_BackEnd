import random

maior = aux = cont = qtde = 0
lista=[]

while cont <=100:
    cont+-1
    aux=int(random.randint(0,100))
    lista.append(aux)  

maior=max(lista)	

while cont <=100:
	cont+-1
	qtde=lista.count(maior) 
	
print('-------------------------------------------------------------------------------------------------')  
print('---------------------- GERANDO NÚMEROS RANDOMICAMENTE E CONTANDO OS TIPOS -----------------------')
print('-------------------------------------------------------------------------------------------------')   
print(f'        O maior número 						é: {maior}')
print(f'        O número {maior} se repete {qtde} vezes na lista')
print(f'        A lista de números é: ')
print(lista)
print('-------------------------------------------------------------------------------------------------') 