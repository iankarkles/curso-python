# Exercício de Adivinhação 2.0 
from random import randint #utilizou apenas o randint, boa ideia - Inspirado do exercício anterior
numero = randint(1,10)
resposta = 0
vezes = 0
print('''Sou seu computador...
Acabei de pensar em um número entre 0 e 10. 
Será que você consegue adivinhar qual foi?
''')
while resposta != numero:
    resposta = int(input("Qual é o seu palpite? "))
    if resposta > numero:
        print("Menos... Tente mais uma vez.")
    elif numero > resposta:
        print("Mais... Tente mais uma vez.")
    vezes = vezes + 1
print(f"Acertou com {vezes} tentativas. Parabéns!")

# Versão do Professor - Se utilizou do Booleano para validar o loop, mais otimizado.Gostei.
from random import randint
computador = randint(0,10)
print('Sou seu computador... Acabeide pensar em um número entre 0 e 10')
print('Será que você consegue adivinhar qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print('Acertou com {} tentativas, parabéns!'.format(palpites))