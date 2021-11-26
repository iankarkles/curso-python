# Resolução do Ian (Usando for por que preguiça né bicho)

n = int(input("Digite um número para ver sua tabuada:"))

tabuada = [1,2,3,4,5,6,7,8,9,10]

print("-------------")
for i in tabuada:
    print("{} x {} = {}".format(n,i,(n*i)))
print("-------------")

#Resolução do professor:

num = int(input("Digite um número para ver a sua tabuada: "))
print('-'*12)
print('{} x {} = {}'.format(num,1,num*1))
print('{} x {} = {}'.format(num,2,num*2))
print('{} x {} = {}'.format(num,3,num*3))
print('{} x {} = {}'.format(num,4,num*4))
print('{} x {} = {}'.format(num,5,num*5))
print('{} x {} = {}'.format(num,6,num*6))
print('{} x {} = {}'.format(num,7,num*7))
print('{} x {} = {}'.format(num,8,num*8))
print('{} x {} = {}'.format(num,9,num*9))
print('{} x {} = {}'.format(num,10,num*10))
print('-'*12)
