#27. Leia um código de cinco algarismos (variável Codigo) e gere o digito verificador (DigitoV) módulo 7 para o mesmo.
#Supondo que os cinco algarismos do código são ABCDE, uma forma de calcular o dígito desejado, com módulo 7 é:
#DigitoV = resto da divisão de S por 7, onde 
#S = 6*A + 5*B + 4*C + 3*D + 2*E 

num = str(input('Informe o código com 5 algarismos: '))

#calculo digito verificador
S = (int(num[0])*6) + (int(num[1])*5) + (int(num[2])*4) + (int(num[3])*3) + (int(num[4])*2)
digito = S%7

novo_num = (str(num)+'-'+str(digito))

print('---------------------------------------------------')
print(f'O número é               : {num}')
print(f'O digito verificador é   : {digito}')
print(f'O novo número é          : {novo_num}')
print('---------------------------------------------------')