numero = input("Digite um número entre 0 e 9999:  ")
#Versão do Ian - Tá feio mas tá funcionando.
numero_separado = list(numero)
numero_separado[0]
if len(numero_separado) == 4:
    print('Unidade: {} '.format(numero_separado[3]))
    print('Dezena: {} '.format(numero_separado[2]))
    print('Centena: {} '.format(numero_separado[1]))
    print('Milhar: {}'.format(numero_separado[0]))
elif len(numero_separado) == 3:
    print('Unidade: {} '.format(numero_separado[2]))
    print('Dezena: {} '.format(numero_separado[1]))
    print('Centena: {} '.format(numero_separado[0]))
elif len(numero_separado) == 2:
    print('Unidade: {} '.format(numero_separado[1]))
    print('Dezena: {} '.format(numero_separado[0]))
elif len(numero_separado) == 1:
    print('Unidade: {} '.format(numero_separado[0]))
else:
    print('Favor digite um número válido!')

#Versão do Professor - Usando módulo (Obs.: Arrojado)

num = int(input('Informe um número: '))
u = num//1 % 10
d = num//10 % 10
c = num//100 % 10
m = num//1000 % 10
print('Analisando o número {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar {}'.format(m))