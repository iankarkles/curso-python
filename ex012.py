#Versão do Ian
preço = float(input("Qual é o preço do produto? R$"))
desconto = preço * 0.95
print("O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}.".format(preço,desconto))

#Versão do professor - Professor utilizou Regra de 3 para a conta, 

#preço = float(input("Qual é o preço do produto? R$")) - Só pra não gastar input
novo = preço - (preço * 5/100)
print("O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}.".format(preço,novo))