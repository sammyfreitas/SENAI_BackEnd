import random
lista=[]                                #criação de uma lista
listapar=[]                             #criação de uma lista para os números pares
listaimpar=[]                           #criação de uma lista para os números ímpares
menor= maior= media = aux = 0           #inicialização de todas as variáveis
for cont in range (0,256):              #loop contador de 0 a 256
    aux=int(random.randint(0,500))      #variavel recebe um valor randomico entre 0 e 500
    lista.append(aux)                   #o comando append adiciona a variavel aux na lista
    if (aux%2==0):                      #condicional para verificar se a variável é par ou ímpar
        listapar.append(aux)            #se a var é par a listapar adiciona essa variável
    else:
        listaimpar.append(aux)          #se a var é ímpar a listaimpar adiciona essa variável

media=round((sum(lista)/len(lista)),2)  #a var média calcula com os comandos sum (soma) / len (qtde de números) o comando round(valor,2 ) arredonda o valor com 2 casas decimais
menor=min(lista)                        #a var menor recebe o menor numero com o comando min()
maior=max(lista)                        #a var maior recebe o maior numero com o comando max()
somaimpar=sum(listaimpar)               #a var somaimpar vai somar todos os itens da listaimpar com o comando sum()

print('-------------------------------------------------------------------------------------------------')  
print('---------------------- GERANDO NÚMEROS RANDOMICAMENTE E CONTANDO OS TIPOS -----------------------')
print('-------------------------------------------------------------------------------------------------')   
print(f'.       A média                           é : {media}')
print(f'        O maior número                    é : {maior}')
print(f'        O menor número                    é : {menor}')
print(f'        A soma dos números ímpares        é : {somaimpar}')
print(f'        A lista de números                é : ')
print(lista)
print('-------------------------------------------------------------------------------------------------') 