frase = "Curso em Vídeo Python"
print(frase[3]) # Para trazer uma letra
print(frase[3:13]) # Para trazer um trecho da String
print(frase[1:15:2]) #Pulando o trecho de 2 em 2 carateres
print(frase[::2]) #Pulando todos os caracteres de 2 em 2

print("Oi")

print('''Olá Andreia, muito obrigado pelo envio das informações, o tablet chegou ontem de tarde conforme o indicado, entretanto a caneta ele está com a ponta solta, impactando na utilização da mesma. Consigo fazer a troca da caneta ou devo pedir a troca do tablet inteiro?''')

print(frase.count("o"))
print(frase.upper().count("O"))
print(len(frase))
frase = "    Curso em Vídeo Python    "
print(len(frase))
print(len(frase.strip()))
print(frase.replace('Python','Android'))
print ('Curso' in frase)
print(frase.find('curso'))
print('curso' in frase)
print(frase.lower().find('curso'))
frase = 'Curso em Vídeo Python'
dividido = (frase.split())
print(dividido)
print(dividido[0])
print(dividido[2][3])
