num1 = int(input("Insira o 1º número: "))
num2 = int(input("Insira o 2º número: "))
num3 = int(input("Insira o 3º número: "))
num4 = int(input("Insira o 4º número: "))
num5 = int(input("Insira o 5º número: "))

media = (num1 + num2 + num3 + num4 + num5)/5

if (media>7):
	print (f'A média é: {media} - Parabéns, Você foi aprovado!')
elif (media>4) and (media<=7):
	print (f'A média é: {media} - Estude Mais, Você está em recuperação!')
else):
	print (f'A média é: {media} - Sinto Muito, Você foi reprovado!')
