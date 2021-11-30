#Exercício do Ian
print('-=-'*20)
print('Analisador de Triângulos')
print('-=-'*20)

s1 = int(input('Primeiro Segmento: '))
s2 = int(input('Segundo Segmento: '))
s3 = int(input('Terceiro Segmento: '))

if ((s1 + s2) > s3) and ((s2 + s3) > s1) and ((s1 + s3) > s2)  :
    print('Os segmentos acima PODEM FORMAR triângulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo!')
#Exercício do Professor

print('-=-'*20)
print('Analisador de Triângulos')
print('-=-'*20)

r1 = int(input('Primeiro Segmento: '))
r2 = int(input('Segundo Segmento: '))
r3 = int(input('Terceiro Segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2: # Fizemos a ordem inversa mas deu no mesmo hehe
        print('Os segmentos acima PODEM FORMAR triângulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo!')
    
