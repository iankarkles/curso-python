# Tarefa do Ian (Obs.: Dólar virou uma variável por que eu esqueci o valor do dia, e na vida real isso seria a resposta de uma API tratada, mas esqueci o valor do exercício hehe)
valor = float(input("Quanto dinheiro você tem na careira? R$"))
dolar = 3.27
print("Com R${} você pode comprar US${:.2f}".format(valor,(valor/dolar)))

# Tarefa do professor - Ele incluiu as casas decimais no real também, boa ideia.
real = float(input('Quanto dinheiro você tem na carteira? '))
dolar = real/3.27
print("Com R${:.2f} você pode comprar US${:.2f}".format(valor,dolar))