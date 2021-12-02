#Versão do Ian
from random import randrange
print('''
Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
''')
opções = ['PEDRA','PAPEL','TESOURA']
jogador = int(input('Qual é a sua jogada? '))
computador = randrange(0,2)
print('''
JO
KEN
PO!!!
-=-=-=-=-=-=-=-=-=-=-=-=-=
Jogador jogou {1}
Computador jogou {0} 
-=-=-=-=-=-=-=-=-=-=-=-=-=
'''.format(opções[computador],opções[jogador])) #Baita solução preguiçosa pra economizar digitação, mas funcionou.
if jogador == computador:
    print('EMPATE')
elif jogador == 0:
    if computador == 1:
        print('COMPUTADOR venceu')
    if computador == 2:
        print('JOGADOR venceu')
elif jogador == 1:
    if computador == 0:
        print('JOGADOR venceu')
    if computador == 2:
        print('COMPUTADOR venceu')
elif jogador == 2:
    if computador == 0:
        print('COMPUTADOR venceu')
    if computador == 1:
        print('JOGADOR venceu')
else:
    print('Por favor, digite uma opção válida!')

#Versão do professor
from random import randint #Por que eu usei randrange invés de randint? Boa pergunta.
itens = ('Pedra','Papel','Tesoura')
computador = randint(0,2)
print('''
Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
''') 
jogador = int(input('Qual é a sua jogada? '))
print('''
JO
KEN
PO!!!
-=-=-=-=-=-=-=-=-=-=-=-=-=
Jogador jogou {}}
Computador jogou {} 
-=-=-=-=-=-=-=-=-=-=-=-=-=
'''.format(itens[jogador],itens[computador])) #Professor incluiu um Sleep de 1 segundo entre as sílabas, porém aqui não incluí pela estrutura do print.
if computador == 0: # Computador jogou PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')
if computador == 1: # Computador jogou PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')
if computador == 2: # Computador jogou TESOURA
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA')
    