#33. O sistema de avaliação de determinada disciplina, é composto por três provas. 
#A primeira prova tem peso 2, 
#a segunda tem peso 3 e 
#a terceira tem peso 5. 
#Faça um algoritmo para calcular a média final de um aluno desta disciplina. 

P1 = float(input('Informe a 1ª prova: '))
P2 = float(input('Informe a 2ª prova: '))
P3 = float(input('Informe a 3ª prova: '))
media=round((((P1*2)+(P2*3)+(P3*5))/10) ,2)
print('---------------------------------------------------')
print(f'A nota da 1ª prova foi   : {P1} e tem Peso 2')
print(f'A nota da 2ª prova foi   : {P2} e tem Peso 3')
print(f'A nota da 3ª prova foi   : {P3} e tem Peso 5')
print(f'A média da discipliana é : {media} ')
print('---------------------------------------------------')