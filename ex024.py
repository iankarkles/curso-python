nome = input("Digite o nome da sua cidade: ")
nome = nome.split()
flag_santo = nome[0] == "Santo" or "santo"
if flag_santo == True:
    print('A cidade em questão começa com Santo')
else:
    print('A cidade em questão não começa com Santo')