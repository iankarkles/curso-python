#Versão do Ian
c = float(input("Informe a temperatura em °C:"))
f = c *1.8 + 32 #Tive que pesquisar na internet por que não lembrava
print("A temperatura de {}°C corresponde a {}°F!".format(c,f))

#Versão do professor

# c = float(input("Informe a temperatura em °C:")) - Pra economizar um input aqui
f = ((9 * c) / 5) + 32
print("A temperatura de {}°C corresponde a {}°F!".format(c,f))