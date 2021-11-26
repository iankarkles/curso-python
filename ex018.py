#Exercício do Ian, depois de vários sufocos

from math import cos,sin,tan,radians

ang = float(input("Digite o ângulo que você deseja: "))
ang = radians(ang)
print("O ângulo de {} tem o SENO de {:.2f}".format(ang, sin(ang)))
print("O ângulo de {} tem o COSSENO de {:.2f}".format(ang, cos(ang)))
print("O ângulo de {} tem a TANGENTE de {:.2f}".format(ang, tan(ang)))

#Exercício do professor:

import math
ângulo = float(input("Digite o ângulo que você deseja: "))
seno = math.sin(math.radians(ângulo))
print("O ângulo de {} tem o SENO de {:.2f}".format(ang, seno))
cosseno = math.cos(math.radians(ângulo))
print("O ângulo de {} tem o COSSENO de {:.2f}".format(ang, cosseno))
tangente = math.tan(math.radians(ângulo))
print("O ângulo de {} tem a TANGENTE de {:.2f}".format(ang, tangente))

#Explicação do professor utilizando o from

#from math import radians,sin,cos,tan

ângulo = float(input("Digite o ângulo que você deseja: "))
seno = sin(radians(ângulo))
print("O ângulo de {} tem o SENO de {:.2f}".format(ang, seno))
cosseno = cos(radians(ângulo))
print("O ângulo de {} tem o COSSENO de {:.2f}".format(ang, cosseno))
tangente = tan(radians(ângulo))
print("O ângulo de {} tem a TANGENTE de {:.2f}".format(ang, tangente))

