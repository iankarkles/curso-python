#Versão do Ian
casa = float(input('Valor da casa: R$'))
salário = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
prestação = casa/(anos*12)
print('Para pagar uma casa de R${:.2f} em {:.0f} anos a prestação será de R${:.2f}'.format(casa, anos, prestação))
if prestação >= (salário * 0.30):
    print('Empréstimo NEGADO!')
else:
    print('Empréstimo pode ser CONCEDIDO!')
#Versão do professor 
