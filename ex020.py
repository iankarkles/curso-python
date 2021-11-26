#Exercício do Ian - tentei com Shuffle e deu erro, dai usei o sample.
from random import sample

a1 = input("Primeiro Aluno: ")
a2 = input("Segundo Aluno: ")
a3 = input("Terceiro Aluno: ")
a4 = input("Quarto Aluno: ")
lista = [a1,a2,a3,a4]
lista_embaralhada = sample(lista,k=4)

print("A ordem de apresentação é: {}".format(lista_embaralhada))

#Exercício do Professor - utilizando o shuffle

from random import shuffle
n1 = input("Primeiro Aluno: ")
n2 = input("Segundo Aluno: ")
n3 = input("Terceiro Aluno: ")
n4 = input("Quarto Aluno: ")

lista = [n1,n2,n3,n4]
shuffle(lista) #Shuffle não recebe variável, por que ele embaralha na própria variável "lista"
print('A ordem de Apresentação será ')
print(lista)