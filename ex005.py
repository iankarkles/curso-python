#Meu Exercício

n = int(input("Digite um valor:"))
antecessor = (n-1)
sucessor = (n+1)
print("Analisando o valor {}, seu antecessor é {} e seu sucessor é {}".format(n,antecessor, sucessor)) 

# Gabarito do professor

n = int(input("Digite um número:"))
a = n - 1 
s = n + 1
print("Analisando o valor {}, seu antecessor é {} e seu sucessor é {}".format(n,a, s)) 

#OU TAMBÉM BOTANDO AS VARIÁVEIS DENTRO DO PRINT

print("Analisando o valor {}, seu antecessor é {} e seu sucessor é {}".format(n,(n-1), (n+1))) 