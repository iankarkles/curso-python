#Exercício do Ian usando While Not - Não cheguei a conclusão de como tirar o último pausa pós exercício.
print('Gerador de PA')
print('-='*15)
numero = int(input('Primeiro Termo:'))
fator = int(input('Qual a razão da PA:'))
contador = 0
total = 10
extra = True
while not contador == total:
    print(f"{numero} --> ",end="")
    numero = numero + fator
    contador += 1
print('PAUSA')
while not extra == 0:
    extra = int(input('Quantos termos você quer mostrar a mais? '))
    total += extra
    while total != contador:
        print(f"{numero} --> ",end="")
        numero += fator
        contador += 1
    print('PAUSA')
print(f"Progressão finalizada com {contador} termos mostrados.")

#Exercício do professor - Professor incluiu o Loop inicial e a a adição na mesma estrutura.
print('Gerador de PA')
print('-='* 10)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
total = 0
cont = 1
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} -> '.format(termo),end='')
        termo += razão
        cont += 1
    print('Pausa')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progresso finalizado com {cont} termos mostrados')