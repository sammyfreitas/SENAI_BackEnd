num1 = int(input("Insira um número: "))
num2 = int(input("Insira outro número: "))
soma_variavel = num1 + num2
if (num1>num2):
    print(f'Número {num1} é maior que {num2}')
elif(num1==num2):
    print(f'Número {num1} é igual a {num2}')
else:
    print(f'Número {num1} é menor que {num2}')
print (f'A soma entre {num1} e {num2} é igual a: {soma_variavel}')