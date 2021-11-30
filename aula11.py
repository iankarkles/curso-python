#CORES NO TERMINAL - Exemplo de código

# \033[0;33;44m - Esse é um exemplo de código para cor no terminal

'''O33 é o código ansi para cor, e na sequência

No primeiro campo temos o estilo do texto:
0 = Nada
1 = Negrito
4 = Sublinado
7 = Negativo

No segundo campo temos a cor do texto:
30 = branco
31 = vermelho
32 = verde
33 = amarelo
34 = azul
35 = roxo
36 = ciano
37 = cinza

No terceiro campo temos o fundo do texto (Background)

40 = branco
41 = vermelho
42 = verde
43 = amarelo
44 = azul
45 = roxo
46 = ciano
47 = cinza
'''

#Aplicação prática:

print('\033[4;30;45m Olá, mundo! \033[m')
