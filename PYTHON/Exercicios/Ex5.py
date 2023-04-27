num1 = int(input("Insira o 1º número: "))
num2 = int(input("Insira o 2º número: "))
num3 = int(input("Insira o 3º número: "))
num4 = int(input("Insira o 4º número: "))
num5 = int(input("Insira o 5º número: "))

media = num1 + num2 + num3 + num4 + num5

print (f'A média entre {num1}, {num2}, {num3}, {num4} e {num5} é igual a: {media}')


----------------------------

cont = int(input("Insira a quantidade de números: "))
soma = 0
for i in range (0,cont):
	soma = soma + int(input('Digite o número: '))
media = soma/cont
print (f'A média é {media}')