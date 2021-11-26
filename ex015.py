#Versão do Ian
dias = float(input("Quantos dias alugados?"))
km = float(input("Quantos Km rodados?"))
valor_km = 0.15
valor_dia = 60

valor = dias * valor_dia + km * valor_km

print("O total a pagar é de R${:.2f}".format(valor))

#Versão do professor

#dias = int(input("Quantos dias alugados?"))
#km = float(input("Quantos Km rodados?")) - Pra economizar os inputs 
pago = (dias * 60) + (km * 0.15)
print("O total a pagar é de R${:.2f}".format(pago))