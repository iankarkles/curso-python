'''
Operadores Aritméticos em Python
+ = Adição
- = Subtração
* = Multiplicação
/ = Divisão
** = Potência
// = Divisão Inteira
% = Resto da divisão
'''
#Exemplos práticos
print(5+2)
print(5-2)
print(5*2)
print(5/2)
print(5**2)
print(5//2)
print(5%2)

'''
Ordem de precedência de operadores aritméticos
1º - ()
2º - **
3º - *,/,//,%
4º - +,-
'''

#Exercício 1 

#5+3*2 = 16 ERRADO
#5+3*2 = 11 CORRETO

print(5+3*2)

'''
Exemplos de aritmética de Python
5+3*2 == 11
3*5+4**2 ==31
3*(5+4)**2 == 243
'''

#Exemplos práticos da aula

print(5+3*2)
#11
print(5**2)
#25
print(5**3)
#125
print(19//2)
#9
print(19/2)
#9.5
print(365**522)
#Um número grande pra caralho só pra mostrar que o INT do python não tem limite de tamanho como no java
print(18%2)
#0
print(122%2)
#2
print(4**3)
#64
print(pow(4,3))
#64, porém utilizando a função de pow(), resumo de power ou potência para fazer a potência dos 2 números na base 2.
print(81**(1/2))
#9.0, retornando a raiz quadrada já que não há um operador específico para raiz quadrada.
print(25**(1/2))
#5.0
print(127**(1/3))
#5.026525....


# UTILIZANDO OPERADORES ARITMÉTICOS COM STRING

print("Oi"+"Olá")
#"OiOlá"
print("Oi"*5)
#OiOiOiOiOiOi
print('='*20)
#=======================

#UTILIZANDO FUNÇÕES EMBUTIDAS NO PRINT

nome = input('Qual o seu nome? ')
print('Prazer em te conhecer {:20}!'.format(nome)) # Nome com no mínimo 20 espaços
print('Prazer em te conhecer {:>20}!'.format(nome)) # vinte espaços e alinhado a direita
print('Prazer em te conhecer {:<20}!'.format(nome)) # vinte espaços e alinhado a esquerda
print('Prazer em te conhecer {:^20}!'.format(nome)) # vinte espaços e alinhado ao centro
print('Prazer em te conhecer {:=^20}!'.format(nome)) # vinte espaços e alinhado ao centro, com o símbolo de "=" em volta (Comentário do Ian: Isso tá parecendo Regex, talvez seja)

#Testes aritméticos

n1 = int(input('Um valor:'))
n2 =int(input('Outro valor:'))
s = n1+n2
m = n1*n2
d = n1/n2
di = n1//n2
e = n1** n2
print("A soma vale {}, \n o produto é {} \n e a divisão é {}".format(s,m,d), end=' ')
print(' a Divisão inteira {}\n e potência {}'.format(di,e))


