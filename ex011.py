largura = float(input("Largura da Parede:"))
altura = float(input("Altura da Parede:"))
print("Sua parede tem a dimensão de {:.2f}X{:.2f} e a sua área é de {:.3f}m² \n Para pintar essa parede, você precisará de {:.4f}l de tinta.".format(largura,altura,(largura*altura),((largura*altura)/2)))

#Também dá pra reduzir isso com 2 prints, deixar mais legível.

#largura = float(input("Largura da Parede:"))
#altura = float(input("Altura da Parede:"))
print("Sua parede tem a dimensão de {:.2f}X{:.2f} e a sua área é de {:.3f}m².".format(largura,altura,(largura*altura)))
print(" Para pintar essa parede, você precisará de {:.4f}l de tinta.".format((largura*altura)/2))


#Resolução do professor

larg = float(input("Largura da Parede:"))
alt = float(input("Altura da Parede:"))
área = larg * alt
print("Sua parede tem a dimensão de {}X{} e a sua área é de {}m².".format(larg,alt,área))
tinta = área/2
print(" Para pintar essa parede, você precisará de {}l de tinta.".format(tinta))