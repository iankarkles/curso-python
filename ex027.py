#Versão do Ian
nome = input('Digite seu nome completo: ')
nome = nome.split()
print('Primeiro nome = {}'.format(nome[0]))
print('Último nome = {}'.format(nome[-1]))

#Versão do Professor:

n = str(input('Digite seu nome completo: ')).strip() #Lembrar de usar o strip!!!
nome = n.split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1])) #Usando o Length -1, melhor do que o -1 nesse momento.




