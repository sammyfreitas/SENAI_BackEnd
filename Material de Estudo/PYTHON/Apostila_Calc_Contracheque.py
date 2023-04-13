# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print('_________________________________________________________')
nome = str(input('Digite o nome do funcionário               : '))
ht = float(input('Digite as Horas Normais Trabalhadas no mês               : '))
vh = float(input('Digite o valor da hora trabalhada                : '))
he50 = float(input('Digite a quantidade de horas extra 50%   '))
he100 = float(input('Digite a quantidade de horas extra 100%   '))
vtd = float(input('Digite o valor de Transporte Diário (ida e volta): '))
dep = int(input('Possui quantos dependentes menores de idade?   '))
print('_________________________________________________________')

#calculo salario bruto
sbruto = round((ht+vh),2)

#calculo horas extras
vhe50=round((he50*(vh*0.5)),2)
vhe100=round((he100*(vh*1)),2)

#calculo salario familia
if (sbruto <=1754.18):
    sfamilia = round((dep*59.82),2)
    msgsalfamilia=''
else
    sfamilia=0.0
    msgsalfamilia='Não tem direito'

#calculo somatorio salarios
total = round((sbruto+he50+he100+sfamilia),2)


#calculo inss
if (sbruto <=1302):
    inss = round((0.075*sbruto),2) #aliquota 7,5%
    aliquota ='7,5%'
elif (sbruto >1302) and (sbruto <2571.30):
    inss = round((0.09*sbruto),2) #aliquota 9%
    aliquota ='9%'
elif (sbruto >=2571.30) and (sbruto <3856.94):
    inss = round((0.12*sbruto),2) #aliquota 12% 
    aliquota ='12%'
else:    
    inss = round((0.14*sbruto),2) #aliquota 14%
    aliquota ='14%'

#calculo vale transporte
vtransp = round((0.06*sbruto),2) #aliquota 6%
vtm = round((vtd*22),2)
if (vtm > vtransp):
    transp=vtransp
else
    transp=vtm


#calculo alimentação
if (sbruto <=6600):
    alim = 36.00
else
    alim = 22*30

#calculo irpf
if (sbruto <=1903.98):
    irpf = 0.0 #aliquota isenta
    aliquota ='Isento'
elif (sbruto >1903.98) and (sbruto <2826.65):
    irpf = round(((sbruto - 1903.98)*0.075),2) #aliquota 7,5%
    aliq_irpf ='7,5%'
elif (sbruto >=2826.65) and (sbruto <3751.05):
    irpf = round(((sbruto - 2826.65)*0.15),2) #aliquota 15%
    aliq_irpf ='15%'
elif (sbruto >=3751.05) and (sbruto <4664.68):
    irpf = round(((sbruto - 3751.05)*0.225),2) #aliquota 22,5% 
    aliq_irpf ='22,5%'
else:    
    irpf = round(((sbruto - 4664.68)*0.275),2) #aliquota 27.5%
    aliq_irpf ='27,5%'
#calculo irpf por dependente
if (dep >0):
    descirpfdep = round((dep*189.59),2)
    irpf=irpf-descirpfdep
#zerando valor irpf caso o valor de desconto seja superior a 0
if (irpf <0):
    irpf=0



#calculo descontos
desc = inss+transp+alim+irpf

#calculo salário liquido
sliq=sbruto-desc

print('----------------------CONTRACHEQUE----------------------')
print(f'FUNCIONÁRIO    :{nome}')
print('_________________________________________________________')
print(f'SALÁRIO BRUTO  : R$ {sbruto}          HORAS TRABALHADAS: {ht}')
print(f'HORAS EXTRAS  50%: R$ {vhe50}         HORAS EXTRAS 50% TRAB: {he50}')
print(f'HORAS EXTRAS 100%: R$ {vhe100}         HORAS EXTRAS 50% TRAB: {he100}')
print(f'SALÁRIO FAMÍLIA: R$ {sfamilia} {msgsalfamilia}          DEPENDENTES: {dep}')
print('_________________________________________________________')
print('DESCONTOS      : R$ {desc}')
print('_________________________________________________________')
print(f'INSS           : R$ {inss}  - Aliquota: {aliquota}')
print(f'IRPF           : R$ {irpf}  - Aliquota: {aliq_irpf}')
print(f'Vale Transporte: R$ {transp} ') 
print(f'Alimentação    : R$ {alim}  ')
print('_________________________________________________________')
print(f'SALÁRIO LÍQUIDO  : R$ {sliq} ')        
print('_________________________________________________________')

