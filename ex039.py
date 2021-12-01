#Versão do Ian

from datetime import date
ano = int(input('Ano de nascimento:'))
ano_atual = date.today().year
idade = ano_atual - ano
print('Quem nasceu em {} tem {} anos em {}'.format(ano,idade,ano_atual))
if idade < 18:
    print('Ainda faltam {} anos para o alistamento.'.format(18-idade))
    print('Seu alistamento será em {}'.format(ano+18))
elif idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
else:
    print('Você já deveria ter se alistado há {} anos'.format(idade-18))
    print('Seu alistamento foi em {}'.format(ano+18))

#Correção do professor - Bem parecido.
# from datetime import date - igual
atual = date.today().year
nasc = int(input('Ano de nascimento:'))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}'.format(nasc,idade,atual))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o alistamento'.format(saldo))
    ano = atual +saldo
    print('Seu alistamento será em {}'.format(ano))
else: #Professor sugere deixar um elif idade > 18 para deixar a compreensão do programa melhor.
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}'.format(ano))
