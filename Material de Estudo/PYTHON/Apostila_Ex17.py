#17. Faça um algoritmo que leia quatro números e apresente os resultados de adição e multiplicação dos valores entre si, baseando-se na utilização da propriedade distributiva, 
#ou seja, se forem lidas as variáveis A, B, C e D, devem ser somadas e multiplicadas A com B, A com C e A com D; B com C, B com D e por último C com D.
#
print('--------------------------------------------------------------------------')
print('-------------------ADIÇÃO E MULTIPLICAÇÃO DISTRIBUTIVA--------------------')
print('--------------------------------------------------------------------------')
A = int(input('Informe o 1º valor : '))
B = int(input('Informe o 2º valor : '))
C = int(input('Informe o 3º valor : '))
D = int(input('Informe o 4º valor : '))
adicao=(A+B)+(A+C)+(A+D)+(B+C)+(B+D)+(C+D)
multiplicacao=(A*B)+(A*C)+(A*D)+(B*C)+(B*D)+(C*D)
print('--------------------------------------------------------------------------')
print(f'A soma distributiva entre os números é           : {adicao}')
print(f'A multiplicação distributiva entre os números é  : {multiplicacao}')
print('--------------------------------------------------------------------------')