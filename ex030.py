# Versão do Ian
n = int(input('Me diga um número qualquer: '))
if (n/2) % 1:
    print('O número {} é IMPAR'.format(n))
else:
    print('O número {} é PAR'.format(n))

# Versão do Professor:

número = int(input('Me diga um número qualquer: '))
resultado = número % 2
if resultado == 0:
    print('O número {} é PAR'.format(número))
else:
    print('O número {} é IM3PAR'.format(número))

