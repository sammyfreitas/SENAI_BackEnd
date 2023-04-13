#39. Suponha que um caixa disponha apenas de notas de 1, 10 e 100 reais.
#Considerando que alguém está pagando uma compra, 
#escreva um algoritmo que mostre o número mínimo de notas que o caixa deve fornecer como troco. 
#Mostre também: 
#o valor da compra, 
#o valor do troco e 
#a quantidade de cada tipo de nota do troco. 
#Suponha que o sistema monetário não utilize moedas.

valor_compra=int(input('Digite o valor da compra: '))
valor_pago=int(input('Digite o valor pago: '))
troco=valor_pago-valor_compra
n_cem=0
n_dez=0
n_um=0
if (troco > 0):
    print(f'O valor do troco é {troco}')
    if (troco >= 100):
        n_cem=troco//100
        troco=troco-(n_cem*100)
        if  (troco > 10):
            n_dez=troco//10
            troco=troco-(n_dez*10)
            if  (troco > 1):
                n_um=troco//1
                troco=troco-(n_um*1)
    elif (troco > 10):
        n_dez=troco//10
        troco=troco-(n_dez*10)
        if  (troco > 1):
            n_um=troco//1
            troco=troco-(n_um*1)
    elif (troco > 1):
        n_um=troco//1
        troco=troco-(n_um*1)
    if (n_cem==0):
        if (n_dez==0):
            print(f'Serão dadas {n_um} notas de R$ 1,00')
        elif (n_dez>0) and (n_um==0):
            print(f'Serão dadas {n_dez} notas de R$ 10,00')
        else:
            print(f'Serão dadas {n_dez} notas de R$ 10,00 e {n_um} notas de R$ 1,00')
    else:
        if (n_dez==0) and (n_um==0):
            print(f'Serão dadas {n_cem} notas de R$ 100,00')
        elif (n_dez>0 and (n_um==0)):
            print(f'Serão dadas {n_cem} notas de R$ 100,00 e {n_dez} notas de R$ 10,00')
        elif (n_dez==0 and (n_um>0)):
            print(f'Serão dadas {n_cem} notas de R$ 100,00 e {n_um} notas de R$ 1,00')
        else:
            print(f'Serão dadas {n_cem} notas de R$ 100,00, {n_dez} notas de R$ 10,00 e {n_um} notas de R$ 1,00')
else:
    print('O valor pago é menor que o valor da compra')