#30. Suponha que uma escola utilize, como código de matrícula, um número inteiro no formato AASDDDD, onde:
#• Os dois primeiros dígitos, representados pela letra A, são os dois últimos algarismos do ano da matrícula;
#• O terceiro dígito, representado pela letra S, vale 1 ou 2, conforme o aluno tenha se matriculado no 1º ou 2º semestre;
#• Os quatro últimos dígitos, representados pela letra D, correspondem à ordem da matrícula do aluno, no semestre e no ano em questão.
#Crie um algoritmo que leia o número de matrícula de um aluno e imprima o ano e o semestre em que ele foi matriculado. 
#
data_lida = str(input('Informe a data no formato AASDDDD: '))
AA = data_lida[0]+data_lida[1]
S = data_lida[2]
print('---------------------------------------------------')
print(f'O ano da matrícula é : {AA}')
print(f'O semestre é         : {S}º Semestre')
print('---------------------------------------------------')