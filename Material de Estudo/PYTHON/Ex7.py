idade = int(input("Digite a idade do atleta: "))
if (idade <5):
	print('Muito jovem para ser atleta')
elif (idade >=5) and  (idade <=10):
	print(f'Idade do atleta: {idade} - Categoria Infantil')
elif (idade >=11) and  (idade <=15):
	print(f'Idade do atleta: {idade} - Categoria Juvenil')
elif (idade >=16) and  (idade <=20):
	print(f'Idade do atleta: {idade} - Categoria Júnior')
elif (idade >=21) and  (idade <=25):
	print(f'Idade do atleta: {idade} - Categoria Júnior')
else:
	print('Passou da idade de ser atleta')