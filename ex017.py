#Exercício do Ian
from math import sqrt
co =float(input("Comprimento do cateto oposto: "))
ca =float(input("Comprimento do cateto Adjacente: "))
#Cálculo da Hipotenusa = Hip² = ca² + co²
hip = sqrt((co**2)+(ca**2))
print("A Hipotenusa vai medir {:.2f}".format(hip))

# Versão do professor

co =float(input("Comprimento do cateto oposto: "))
ca =float(input("Comprimento do cateto Adjacente: "))
hi = (co ** 2 + ca ** 2) ** (1/2)
print("A Hipotenusa vai medir {:.2f}".format(hi))

#USANDO A CLASSE HYPOT DO MATH

from math import hypot
co =float(input("Comprimento do cateto oposto: "))
ca =float(input("Comprimento do cateto Adjacente: "))
hi = hypot(co,ca)
print("A Hipotenusa vai medir {:.2f}".format(hi))


