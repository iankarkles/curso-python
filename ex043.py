#Versão do Ian
peso = float(input('Qual é o seu peso? (Kg)'))
altura = float (input('Qual é a sua altura? (m)'))

imc = peso/(altura**2)

print('O IMC dessa pessoa é {:.1f}'.format(imc))

if imc < 18.5:
    print('Você está ABAIXO DO PESO normal')
elif 18.5 <= imc < 25:
    print('PARABÉNS, você está na faixa de PESO NORMAL')
elif 25 <= imc < 30:
    print('Você está em SOBREPESO')
elif 30 <= imc < 40:
    print('Você está em OBESIDADE, cuidado!')
else:
    print('Você está em OBESIDADE MÓRBIDA, cuidado!')
# Versão do Professor - Pouca variação, apenas um elif a mais para deixar o código legível

peso = float(input('Qual é o seu peso? (Kg)'))
altura = float (input('Qual é a sua altura? (m)'))

imc = peso/(altura**2)
print('O IMC dessa pessoa é {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO normal')
elif 18.5 <= imc < 25:
    print('PARABÉNS, você está na faixa de PESO NORMAL')
elif 25 <= imc < 30:
    print('Você está em SOBREPESO')
elif 30 <= imc < 40:
    print('Você está em OBESIDADE!')
elif imc >= 40:
    print('Você está em OBESIDADE MÓRBIDA, cuidado!')
