#Versão do Ian, pesquisou na biblioteca math pra descobrir como fazia.
from math import trunc

n = float(input("Digite um valor:"))
i = trunc(n)

print("O valor digitado foi {} e a sua parte inteira é {}".format(n,i))

# Versão do professor

# import math ele começou com exemplo mas depois fez a importação do trunc só
num = float(input("Digite um valor: "))
print("O valor digitado foi {} e a sua porção inteira é {}".format(num, trunc(num)))

#Fazer o programa sem a importação da biblioteca math

num = float(input("Digite um valor: "))
print("O valor digitado foi {} e a sua porção inteira é {}".format(num,int(num)))