frase = input("Digite uma frase: ")

print("A Letra A aparece {} vezes.".format(frase.lower().count('a')))

print('A primeira vez que a Letra A aparce é na posição {}'.format(frase.lower().find("a")))

print('A última vez que a Letra A aparce é na posição {}'.format(frase.lower().rfind("a")))