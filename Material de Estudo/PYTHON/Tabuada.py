resp='s'
while (resp=='S') or (resp=='s'):
    tabuada=int(input('Digite o número da tabuada: '))
    print(f'-------TABUADA DE {tabuada} -------')
    num=0    
    while (num <=10):
        print(f'{num} x {tabuada} = {num*tabuada}')
        num +=1
    resp=str(input('Deseja continuar? [S/N] '))
print(f'Obrigado por testar a tabuada de {tabuada}')t