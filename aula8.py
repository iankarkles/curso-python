#Exemplo de importação da biblioteca Math
import math
num = int(input("Digite um número: "))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {:.2f}'.format(num,raiz))

#Exemplo de importação do From/Import
from math import sqrt
num = int(input("Digite um número: "))
raiz = sqrt(num)
print('A raiz de {} é igual a {:.2f}'.format(num,raiz))

# Exemplo importação random

import random

num = random.random()
print(num)

num = random.randint(1,10)
print(num)

#baixando bibliotecas externas

import emoji
print(emoji.emojize("Olá mundo :earth_americas:", use_aliases=True))

