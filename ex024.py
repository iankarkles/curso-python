#Versão do Ian
nome = input("Digite o nome da sua cidade: ")
nome = nome.split()
flag_santo = nome[0].lower() == "santo"
if flag_santo == True:
    print('A cidade em questão começa com Santo')
else:
    print('A cidade em questão não começa com Santo')

#Versão do professor - bem mais curta

cid = str(input('Em que cidade você nasceu? ')).strip()
print(cid[:5].upper() == 'SANTO')
