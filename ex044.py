#Versão do Ian
print(10*'=',end="")
print(' LOJAS GUANABARA ', end='')
print(10*'=')
preço = float(input('Preço das compras: R$'))
print('''
FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão
''')

final = 0
opcao = int(input('Qual é a opção?'))
if opcao == 1:
    final = preço * 0.9
if opcao == 2:
    final = preço * 0.95
if opcao == 3:
    final = preço * 1
if opcao == 4:
    final = preço * 1.2
    quantidade = int(input('Qual a quantidade de parcelas?'))
    valor_parcela = final/quantidade
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(quantidade,valor_parcela))
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço,final)) # Prestar atenção na formatação dos números. (Caso contrário: ValueError Format specifier missing precision)

#Versão do professor:
print('{:=^40}'.format(' LOJAS GUANABARA ')) #Registrar essa dica para títulos! ^ para centralizar e o símbolo antes para utilizar
preço = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual é a opção?'))
if opcao == 1:
    total = preço - (preço * 10/100)
elif opcao == 2:
    total = preço - (preço * 5/100)
elif opcao == 3:
    total = preço
    parcela =total/2
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(parcela))
elif opcao == 4:
    total = preço + (preço * 20/100)
    totalparc = int(input('Qual a quantidade de parcelas?'))
    parcela = total / totalparc
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(quantidade,valor_parcela))
else: #Incluir else é sempre interessante
    total = 0
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente!')

print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço,total))

