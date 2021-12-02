#Exercício do Ian
print('-=-'*20)
print('Analisador de Triângulos')
print('-=-'*20)

s1 = int(input('Primeiro Segmento: '))
s2 = int(input('Segundo Segmento: '))
s3 = int(input('Terceiro Segmento: '))

tipo = ""
if s1 == s2 == s3:
    tipo = 'EQUILÁTERO'
elif s1 == s2 or s1 == s3 or s2 == s3:
    tipo = 'ISÓCELES'
else:
    tipo = 'ESCALENO'

if ((s1 + s2) > s3) and ((s2 + s3) > s1) and ((s1 + s3) > s2)  :
    print(f'Os segmentos acima PODEM FORMAR um triângulo {tipo}')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo!')

#versão do Professor

r1 = float(input('Primeiro Segmento: '))
r2 = float(input('Segundo Segmento: '))
r3 = float(input('Terceiro Segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR triângulo ',end='')
    if r1 == r2 == r3: # Incluído outro IF dentro do primeiro IF - IF Aninhado
        print('EQUILÁTERO!')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO!')
    else:
        print('ISÓCELES') # Não preciso testar o Isóceles, inteligente.
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo')