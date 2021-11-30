# Versão do Ian
dist = float(input('Qual é a distância da sua viagem?'))
if dist < 200:
    print ('Você está prestes a começar uma viagem de {}km'.format(dist))
    print('E o preço da sua passagem será de {}'.format(dist*0.50))
else:
    print ('Você está prestes a começar uma viagem de {}km'.format(dist))
    print('E o preço da sua passagem será de R${:.2f}'.format(dist*0.45))

# Versão do professor:

distância = float(input('Qual é a distância da sua viagem?'))
print ('Você está prestes a começar uma viagem de {}km'.format(distância))
if distância < 200:
    preço = distância *0.50
else:
    preço = distância *0.45

print('E o preço da sua passagem será de R${:.2f}'.format(preço)) # Retirar as caixas de texto desnecessárias
preço = distância *0.50 if distância <= 200 else distância *0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preço))