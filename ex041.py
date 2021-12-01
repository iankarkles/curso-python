from datetime import date
nasc = int(input('Ano de Nascimento:'))
atual = date.today().year
idade = atual - nasc
print('O atleta tem {} anos.'.format(idade))
classe = ''
if idade < 9:
    classe = 'Mirim'
    #Mirim
elif idade < 14:
    classe = 'Infantil'
    #Infantil
elif idade < 19:
    classe = 'Junior'
    #Junior
elif idade < 25:
    classe = 'Sênior'
    #Sênior
else:
    classe = 'Master'
    #Master
print('Classificação: {}'.format(classe))

#Versão do professor

#from datetime import date - pra não repetir
nasc = int(input('Ano de Nascimento:'))
atual = date.today().year
idade = atual - nasc
print('O atleta tem {} anos.'.format(idade))
if idade <= 9: #Até nove, na minha interpretação o 9 não entra
    print('Classsificação: MIRIM')
elif idade <= 14:
    print('Classsificação: INFANTIL')
elif idade <= 19:
    print('Classsificação: JUNIOR')
elif idade <= 25:
    print('Classsificação: SÊNIOR')
else:
    print('Classsificação: MASTER')