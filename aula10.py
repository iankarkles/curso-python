#Parte teórica

tempo = int(input('Quantos anos tem seu carro?'))
if tempo <= 3:
    print('Carro novo')
else:
    print('Carro velho')
print('--Fim--')

#Utilizando uma condição aninhada

tempo = int(input('Quantos anos tem seu carro?'))
print ('Carro novo' if tempo <= 3 else 'Carro velho')
print('--Fim--')

#Prática - Exercício 1
nome =str(input('Qual o seu nome?'))
if nome == 'Ian':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal!')
print('Bom dia, {}'.format(nome))

#Exemplo 2

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('A sua média foi {:.1f}'.format(m))
if m >= 6.0:
    print('A sua média foi boa! PARABÉNS!')
else:
    print('Sua média foi ruim! ESTUDE MAIS!')
print('PARABÉNS'if m >= 6 else 'ESTUDE MAIS')