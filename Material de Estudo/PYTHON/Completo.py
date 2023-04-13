N1 = int(input("Insira o primeiro número: "))
N2 = int(input("Insira o segundo número: "))
N3 = int(input("Insira o terceiro número: "))
lista=[N1,N2,N3]
maior = N1
if N2 > N1 and N2 > N3:
    maior = N2
if N3 > N1 and N3 > N2:
    maior = N3
menor = N1
if N2 < N3 and N2 < N1:
    menor = N2
if N3 < N2 and N3 < N1:
    menor = N3
print('------------------------------------------------')
print(f'Os números digitados foram {N1}, {N2}, {N3}')
print('------------------------------------------------')
print(f'O menor número digitado foi {menor}')
print(f'O maior número digitado foi {maior}')
print('------------------------------------------------')
print('A lista em ordem crescente é ',sorted(lista))
print('A lista em ordem decrescente é ',sorted(lista, reverse=True))
print('------------------------------------------------')