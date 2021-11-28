#Versão do Ian
nome = input("Digite um nome: ")

if nome.lower().find('silva') != -1:
    print('O nome em questão contém Silva')
else:
    print('O nome em questão não contém Silva')

# Versão do professor - Do jeito certo

nome = str(input('Qual é o seu nome completo? ')).strip()
print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))

