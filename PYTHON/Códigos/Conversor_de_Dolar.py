# Conversor de D�lar
# http://www.codigofree.com
# Criado por Anderson Ferreira (andersonferreira631@yahoo.com.br)

# Abaixo encontra-se o script de um Conversor de D�lar, bastante simples.

# A letra "d" indica o valor do d�lar.
# O n�mero "10" indica o valor (de 0 � 10) que ser� convertido de D�lar para Reais.



# ---------------- #
# In�cio do Script
# ---------------- #


d = 2.2939989

for p in range(10): print 'US$ %5.2f = R$ %5.2f' % (p, p * d)
print '-' * 20


# ---------------- #
# Fim do Script
# ---------------- #