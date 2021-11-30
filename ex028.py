#Versão do Ian
import random
print('Vou pensar em um número inteiro entre 0 e 5. Tente adivinhar...')
n = random.randint(0,5)
n_user = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
if n == n_user:
    print('Parabéns! Você conseguiu me vencer!')
else:
    print('Ganhei! Eu pensei no número {} e não no {}!'.format(n,n_user))

# Versão do professor

from random import randint #utilizou apenas o randint, boa ideia
from time import sleep
computador = randint(0,5) # Faz o computador "PENSAR"
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-'*20)
jogador = int(input('Em que número eu pensei? ')) # Jogador tenta adivinhar
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}'.format(computador, jogador))

