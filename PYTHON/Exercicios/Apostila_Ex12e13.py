#12. Faça um algoritmo que leia uma temperatura em graus Celsius e apresente-a convertida em graus Fahrenheit.
#A fórmula de conversão é: F = (9 * C + 160) / 5,na qual F é a temperatura em Fahrenheit e C é a temperatura em Celsius;
#
#13. Faça um algoritmo que leia uma temperatura em Fahrenheit e a apresente convertida em graus Celsius. 
#A fórmula de conversão é C = (F – 32) * ( 5 / 9), na qual F é a temperatura em Fahrenheit e C é a temperatura em Celsius. 
#
print('--------------------------------------------')
print('-------------CONVERSÃO DE GRAUS-------------')
print('--------------------------------------------')
print('''
        MENU:
        [1] - CELSIUS EM FARENHEIT
		[2] - CELSIUS EM KELVIN
		[3] - FARENHEIT EM CELSIUS
		[4] - FARENHEIT EM KELVIN
		[5] - KELVIN EM CELSIUS
        [6] - KELVIN EM FARENHEIT
        [7] - Sair
	''')
opcao = int(input('Escolha uma opção: '))

if (opcao==1):
    temp = float(input('Digite a temperatura: '))    
    tempconv = round((((temp*9)/5)+32),2)
    print(f'Celsius: {temp}ºC = Farenheit: {tempconv}ºF')
    print('--------------------------------------------')
elif (opcao==2):
    temp = float(input('Digite a temperatura: '))    
    tempconv = round((temp+273.15),2)
    print(f'Celsius: {temp}ºC = Kelvin: {tempconv}ºK')
    print('--------------------------------------------')
elif (opcao==3):
    temp = float(input('Digite a temperatura: '))    
    tempconv = round((((temp-32)*5/9)),2)
    print(f'Farenheit: {temp}ºF = Celsius: {tempconv}ºC')
    print('--------------------------------------------')
elif (opcao==4):
    temp = float(input('Digite a temperatura: '))    
    tempconv = round((((temp-32)*5/9)+273.15),2)
    print(f'Farenheit: {temp}ºF = Kelvin: {tempconv}ºK')
    print('--------------------------------------------')
elif (opcao==5):
    temp = float(input('Digite a temperatura: '))    
    tempconv = round((temp-273.15),2)
    print(f'Kelvin: {temp}ºK = Celsius: {tempconv}ºC')
    print('--------------------------------------------')
elif (opcao==6):
    temp = float(input('Digite a temperatura: '))    
    tempconv = round((((temp-273.15)*9/5)+32),2)
    print(f'Kelvin: {temp}ºK = Farenheit: {tempconv}ºF')
    print('--------------------------------------------')

elif (opcao==7):
    print('Obrigado por calcular! Volte Sempre!')
    print('--------------------------------------------')
else:
    print('Opção Inválida')
    print('--------------------------------------------')