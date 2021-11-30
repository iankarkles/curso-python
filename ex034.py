salario = float(input('Qual é o salário do funcionário? R$'))
if salario > 1250.0:
    print('Quem ganhava R${} passa a ganhar R${}'.format(salario,(salario*1.10))) #10% de aumento
else:
    print('Quem ganhava R${} passa a ganhar R${}'.format(salario,(salario*1.15))) #15% de aumento
#Versão do professor
salário = float(input('Qual é o salário do funcionário? R$'))
if salário <= 1250:
    novo = salário + (salário * 15/100)
else:
    novo = salário + (salário * 10/100)
print('Quem ganhava R${} passa a ganhar R${}'.format(salario,novo)) # Professor economizou um print aqui, boa ideia.

