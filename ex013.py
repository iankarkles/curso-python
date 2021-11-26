#Exercício do Ian
salario = float(input("Qual é o salário do Funcionário R$"))
novo = salario * 1.05
print("Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}".format(salario,novo))

#Exercício do professor - Também usou regra de três.

salário = float(input("Qual é o salário do Funcionário R$"))
novo = salário + (salário*15/100)
print("Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}".format(salário,novo))