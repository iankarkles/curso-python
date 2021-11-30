#Versão do Ian
vel = int(input('Qual a velocidade atual do carro? '))
if  vel >= 80: # Errei aqui, era pra ser só maior
    print('MULTADO! Você excedeu o limite permitido que é de 80km/h \n Você deve pagar uma multa de R${:.2f}!'.format((vel-80)*7.00))
else:
    print('Tenha um bom dia! Dirija com segurança!')
#Versão do professor
velocidade = float(input('Qual é a velocidade atual do carro? '))
if velocidade >= 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80 km/h')
    multa = (velocidade - 80) * 7
    print('Você deve pagar uma multa de R${:.2f}!'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')