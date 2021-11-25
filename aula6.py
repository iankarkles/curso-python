# Como não funciona a soma de números. - Desafio Aula 4
n1 = input('Por favor, digite um número: ')
n2 = input('Por favor, digite outro número: ')
print(type(n1))
s = n1+n2
print ("A soma é",s)

#Sugestão do professor - Transformar as entradas em Inteiro:
n1 = int(input('Por favor, digite um número: '))
n2 = int(input('Por favor, digite outro número: '))
s = n1+n2
print ("A soma é",s)
print("A soma vale {}".format(s))

print ("A soma entre {} e {} vale {}".format(n1,n2,s))


# Teste de validação - Alfanumérico

n = input('digite algo:')

print(n.isalnum())