""""
2- Suponha que o conceito de um aluno seja determinado em função da sua nota. 
Suponha, também, que esta nota seja um valor inteiro na faixa de 0 a 100, 
conforme a seguinte faixa: 
 Nota Conceito
 0 a 49 Insuficiente 
 50 a 64 Regular 
 65 a 84 Bom 
 85 a 100 Ótimo 
"""
nome=str(input('Digite o nome do aluno : '))
nota=int(input('Digite a nota do aluno : '))
if ((nota==0) and (nota<49)):
    msg='Insuficiente'
elif ((nota>=50) and (nota<64)):
    msg='Regular'
elif ((nota>=65) and (nota<84)):
    msg='Bom'
else:
    msg='Ótimo'
    
print('-------------------------- CONCEITO -------------------------------')
print(f'Aluno           : {nome}')
print(f'Nota		    : {nota}')
print(f'Conceito		: {msg}')
print('-------------------------------------------------------------------')   