# Exercício do Ian
n = int(input("Digite um número:"))
d = n*2
t = n*3
r = n**(1/2)
print("O dobro de {} é {}".format(n,d))
print("O triplo de {} é {}".format(n,t))
print("A raiz quadrada de {} é {}".format(n,r))

# Exercício do Professor

#n = int(input("Digite um número:")) (Pra evitar 2 inputs redudantes no código)
d = n*2
t = n*3
r = n**(1/2)
print("O dobro de {} vale {}".format(n,d))
print("O triplo de {} vale {}. \nA raiz quadrada de {} é igual a {:.2f}.".format(n,t,n,r))