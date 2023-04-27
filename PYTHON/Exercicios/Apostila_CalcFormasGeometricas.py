# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
#def menu():
print('--------------------------------------------')
print('---------CALCULO FORMAS GEOMÉTRICAS---------')
print('--------------------------------------------')
print('''
        MENU:
        [1] - Circulo
		[2] - Retângulo
		[3] - Triângulo
		[4] - Quadrado
		[5] - Pentágono Regular
        [6] - Hexágono Regular
        [7] - Sair
	''')
opcao = int(input('Escolha uma opção: '))

#def main()
#while (opcao!=7)
if (opcao==1):
    raio = float(input('Digite o Raio: '))
    pi = 3.14159
    area = round((pi*(raio*raio)),2)
    perimetro = round((2*pi*raio),2)
    print(f'A área do Círculo de Raio [{raio}] é {area} e seu perímetro é {perimetro}')
    #op = str(input('Escolha uma opção: s/n'))
    #if (op=='s')
    #    menu()
    #else
    #    break
elif (opcao==2):
    ldmaior = int(input('Digite o Lado Maior: '))
    ldmenor = int(input('Digite o Lado Menor: '))
    area = round((ldmaior*ldmenor),2)
    perimetro = round(((2*ldmaior)+(2*ldmenor)),2)
    print(f'A área do Retângulo de Lados [{ldmaior} e {ldmenor}] é {area} e seu perímetro é {perimetro}')
    #op = str(input('Escolha uma opção: s/n'))
    #if (op=='s')
    #    menu()
    #else
    #    break
elif (opcao==3):
    base = float(input('Digite a Base: '))
    altura = float(input('Digite a Altura: '))
    area = round(((base*altura)/2),2)
    ldigual = str(input('É um triângulo equilátero? (os três lados são iguais) s/n : '))
    if (ldigual=='s'):
        l1 = float(input('Digite o Lado: '))
        perimetro =round((3*l1),2)
        print(f'A área do Triângulo de Lados Iguais [{l1}], é {area} e seu perímetro é {perimetro}')
    elif (ldigual=='n'):
        l1 = float(input('Digite o primeiro Lado: '))
        l2 = float(input('Digite o segundo Lado: '))
        l3 = float(input('Digite o terceiro Lado: '))
        perimetro = round((l1+l2+l3),2)
        print(f'A área do Triângulo de Lados Diferentes [{l1}, {l2} e {l3}] é {area} e seu perímetro é {perimetro}') 
    else:
        print('Opção Inválida')
        #op = str(input('Escolha uma opção: s/n'))
        #if (op=='s')
        #    menu()
        #else
        #    break
elif (opcao==4):
    lado = float(input('Digite o Lado: '))
    perimetro = round((4*lado),2)
    area = round((lado*lado),2)
    print(f'A área do Quadrado de Lado [{lado}] é {area} e seu perímetro é {perimetro}')
        #op = str(input('Escolha uma opção: s/n'))
        #if (op=='s')
        #    menu()
        #else
        #    break
elif (opcao==5):
    lado = float(input('Digite o Lado: '))
    apotema = float(input('Digite o Apótema: '))
    perimetro = round((5*lado),2)
    area = round(((perimetro*apotema)/2),2)
    print(f'A área do Pentágono Regular de Lado [{lado}] e Apótema [{apotema}] é {area} e seu perímetro é {perimetro}')
        #op = str(input('Escolha uma opção: s/n'))
        #if (op=='s')
        #    menu()
        #else
        #    break
elif (opcao==6):
    lado = float(input('Digite o Lado: '))
    apotema = float(input('Digite o Apótema: '))
    perimetro = round((6*lado),2)
    area = round(((perimetro*apotema)/2),2)
    print(f'A área do Hexágono Regular de Lado {lado} e Apótema {apotema} é {area} e seu perímetro é {perimetro}')
        #op = str(input('Escolha uma opção: s/n'))
        #if (op=='s')
        #    menu()
        #else
        #    break
elif (opcao==7):
    print('Obrigado por Calcular')
else:
    print('Opção Inválida')