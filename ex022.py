
#Versão do Ian
nome = input("Digite seu nome completo: ")
print(nome.upper())
print(nome.lower())
dividido = nome.split()
nome = "".join(dividido)
print(len(nome))
print(len(dividido[0]))

# Versão do professor

nome = str(input('Digite seu nome completo: ')).strip() #Pra evitar incluir espaços antes e depois - Não pensei nisso :c
print('Analisando seu nome...')
print('Seu nome em maiusculas é {}'.format(nome.upper()))
print('Seu nome em minusculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' '))) #Desse jeito ele resolve o problema do strip também, inteligente e mais prático do que a gambiarra de separar e juntar os splits.
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0],len(separa[0])))
