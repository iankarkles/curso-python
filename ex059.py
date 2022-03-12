# Versão do Ian arrojada, bem provável que dê pra fazer bem melhor.
from math import factorial
numero = int(input('Digite um número para calcular o seu fatorial: '))
base = 1
fatorial = factorial(numero)
print(f'Calculando {numero}! = ',end='')
while not numero == base:
    print(numero,end='')
    print(' X ',end='')
    numero -= 1
print(f"1 = {fatorial}")

# Versão do professor sem importar fatorial
n = int(input('Digite um número para calcular seu fatorial: '))
c = n
f = 1

print('Calculando {}! = '.format(n),end='')
while c > 0:
    print(' {} '.format(c),end='')
    print(' x ' if c > 1 else ' = ', end="")
    f *= c
    c -= 1
print('{}'.format(f))
