#Minha tentativa

str = input("Digite algo: ")
print("O tipo primitivo desse dado é {}".format(type(str)))
print("Só tem espaços? {}".format(str.isspace()))
print("Só tem números? {}".format(str.isnumeric()))
print("Só tem alfabéticos? {}".format(str.isalpha()))
print("É alfanúmerico? {}".format(str.isalnum()))
print("Está em maiúsculas? {}".format(str.isupper()))
print("Está em minuúsculas? {}".format(str.islower()))
print("Está capitalizada? {}".format(str[0].isupper()))


#Código do professor
 
 
str = input("Digite algo: ")
print("O tipo primitivo desse dado é {}".format(type(str)))
print("Só tem espaços? {}".format(str.isspace()))
print("Só tem números? {}".format(str.isnumeric()))
print("Só tem alfabéticos? {}".format(str.isalpha()))
print("É alfanúmerico? {}".format(str.isalnum()))
print("Está em maiúsculas? {}".format(str.isupper()))
print("Está em minuúsculas? {}".format(str.islower()))
print("Está capitalizada? {}".format(str.istitle()))

#Meu código não pegaria outras palavras da frase que não fossem capitalizadas, enquanto o istitle() sim. importante verificar isso.