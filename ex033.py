from time import time
#Exercício do Ian
n1 = int (input('Primeiro valor: '))
n2 = int (input('Segundo valor: '))
n3 = int (input('Terceiro valor: '))

inicio = time()

lista = [n1, n2, n3]
lista.sort()

print('O menor valor digitado foi {} '.format(lista[0]))
print('O maior valor digitado foi {} '.format(lista[2]))

fim = time()

print('duracao: %f' % (fim - inicio))
#Exercício do Professor

a = int (input('Primeiro valor: '))
b = int (input('Segundo valor: '))
c = int (input('Terceiro valor: '))

inicio = time()
# Verificando quem é o menor - professor usou um caminhão de condicionais, enquanto eu fui de lista hehe
menor = a
if b<a and b<c:
    menor  = b
if c<a and c<b:
    menor = c
#Verificando quem é o maior - professor usou as condicionais invertidas pro maior número
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print('O menor valor digitado foi {} '.format(menor))
print('O maior valor digitado foi {} '.format(maior))
fim = time()

print('duracao: %f' % (fim - inicio)) #Fiz por conta própria pra ver o que era mais funcional, porém as 2 são tão irrisórias que não tem diferença no tempo das funções.




