#Versão do Ian
frase = input("Digite uma frase: ").strip()

print("A Letra A aparece {} vezes.".format(frase.lower().count('a')))

print('A primeira vez que a Letra A aparce é na posição {}'.format(frase.lower().find("a")))

print('A última vez que a Letra A aparce é na posição {}'.format(frase.lower().rfind("a")))

#Versão do Professor

frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes na frase.'.format(frase.count('A')+1)) #Para desconsiderar o Zero como posição.
print('A última letra A apareceu na posição {}'.format(frase.rfind('A')+1)) #Para desconsiderar o Zero como posição.