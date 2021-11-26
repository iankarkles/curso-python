#Exercício do Ian

metros = float(input("Digite uma distância em metros:"))
'''
(essa parte eu vi que era denecessária enquanto estava debugando o projeto, faltava as virgulas dentro do format e por isso não estava funcionando)
km = (metros/1000)
hm = (metros/100)
dam = (metros/10)
dm = (metros*10)
cm = (metros*100)
mm = (metros*1000)
'''
print("{:.3f}km\n{:.2f}hm\n{:.1f}dam\n{:.0f}dm\n{:.0f}cm\n{:.0f}mm\n".format((metros/1000),(metros/100),(metros/10),(metros*10),(metros*100),(metros*1000)))

#Exercício do Professor - Ele não fez o exercício inteiro (Acho)

medida = float(input('Uma Distância em metros: '))
cm = medida * 100
mm = medida * 1000
print(' A medida de {}m corresponde a {:.0f}cm e {:.0f}mm'.format(medida,cm,mm))

