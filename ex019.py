#Exercício do Ian
from random import choice

a1 = input("Primeiro Aluno: ")
a2 = input("Segundo Aluno: ")
a3 = input("Terceiro Aluno: ")
a4 = input("Quarto Aluno: ")

print("O aluno escolhido foi: {}".format(choice([a1,a2,a3,a4])))

#Exercício do professor

#from random import choice

n1 = str(input("Primeiro aluno: "))
n2 = str(input("Segundo aluno: "))
n3 = str(input("Terceiro aluno: "))
n4 = str(input("Quarto aluno: "))
lista = [n1,n2,n3,n4]
escolhido = choice(lista)
print("O aluno escolhido foi: {}".format(escolhido))
