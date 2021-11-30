#Versão do Ian, apanhei com o year, por que achei que fosse um método, porém não deve ser chamado.
from datetime import datetime
ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = datetime.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0: #Incluí depois as demais condições para ser bissexto, ano multiplo de 100 que não é múltiplo de 400.
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} não é BISSEXTO'.format(ano))
#Versão do professor

ano = int(input('Que ano quer analisar? '))
if ano == 0:
    ano = datetime.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0: #Incluídas as outras condições pro ano não ser Bissexto
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} não é BISSEXTO'.format(ano))