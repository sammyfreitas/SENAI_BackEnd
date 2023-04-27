#28. Dado um número de três algarismos N = CDU (onde C é o algarismo das centenas, D é o algarismo das dezenas e U o algarismo das unidades), considere o número M constituído pelos algarismos de N em ordem inversa, isto é, M = UDC. Gerar M a partir de N (p.ex.: N = 123 -> M = 321). 

N = str(input('Informe a centena: '))
C = N[0]
D = N[1]
U = N[2]
M = str(U+D+C)
print('---------------------------------------------------')
print(f'O número é               : {N}')
print(f'O novo número é          : {M}')
print('---------------------------------------------------')