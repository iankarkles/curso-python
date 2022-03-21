#Exercício do Ian usando While Not
print('Gerador de PA')
print('-='*15)
numero = int(input('Primeiro Termo:'))
fator = int(input('Qual a razão da PA:'))
contador = 0
verificacao = False

while not contador == 10:
    print(f"{numero} --> ",end="")
    numero = numero + fator
    contador += 1
print('FIM')

#Versão do professor

print('Gerador de PA')
print('-='* 10)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
const = 1
while const <= 10:
    print('{} ->'.format(termo),end='')
    termo = termo + razão
    const += 1
print('FIM')