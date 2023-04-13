#35. Considere que o último concurso vestibular apresentou três provas: Português, Matemática e Conhecimentos Gerais. 
#Considerando que para cada candidato tem-se um registro contendo o seu nome e as notas obtidas em cada uma das provas, 
#construa um algoritmo que forneça:
#a) o nome e as notas em cada prova do candidato
#b) a média do candidato
#c) uma informação dizendo se o candidato foi aprovado ou não. 
#Considere que um candidato é aprovado se sua média for maior que 7.0 e se não apresentou nenhuma nota abaixo de 5.0 

nome=str(input('Digite o nome do aluno                : '))
port=float(input('Digite a nota de Português            : '))
mat=float(input('Digite a nota de Matemática           : '))
c_gerais=float(input('Digite a nota de Conhecimentos Gerais : '))
media=round(((port+mat+c_gerais)/3),2)
if ((media>=7) and (port>5) and (mat>5) and (c_gerais>5)):
    msg='Candidato Aprovado'
else:
    msg='Candidato Reprovado'
    if(media<7):
        msg2='Média'
    elif (port<=5):
        msg2='Nota de Português'
    elif (mat<=5):
        msg2='Nota de Matemática'
    else:
        msg2='Nota de Conhecimentos Gerais'
    
print('-------------------------- VESTIBULAR 2023 -------------------------------')
print(f'Aluno                       : {nome}')
print(f'Nota de Português           : {port}')
print(f'Nota de Matemática          : {mat}')
print(f'Nota de Conhecimentos Gerais: {c_gerais}')
print(f'Média                       : {media}')
print(f'Status                      : {msg} por {msg2}')
print('--------------------------------------------------------------------------')  




""""
vestibular={'nome': Anthony,
            'port': 9.6,
            'mat': 9.8,
            'c_gerais': 9.5,
            'media':
            }

[Anthony,9.0,10.0,9.5]


print('--------------------------------------------------------------')
print('-----------------------VESTIBULAR 2023------------------------')
print('--------------------------------------------------------------')
print('''
        MENU:
        [1] - Cadastro Vestibular
		[2] - Consulta Individual
		[3] - Consulta Aprovados
		[4] - Consulta Reprovados
		[5] - Sair
	''')
opcao = int(input('Escolha uma opção: '))

if (opcao==1):
    cont=int(input('Digite a quantidade de alunos a ser cadastrada : '))
    vestibular={}
    i=0
    while (i!=cont):
        vestibular['nome']=str(input('Digite o nome do aluno     : '))
        vestibular['port']=float(input('Digite a nota de Português : '))
        vestibular['mat']=float(input('Digite a nota de Matemática : '))
        vestibular['c_gerais']=float(input('Digite a nota de Conhecimentos Gerais : '))
        vestibular['media']=((vestibular['port'])+vestibular['mat']+vestibular['c_gerais'])/3
        i=i+1