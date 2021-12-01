#Versão do Ian
n1 = float(input('Primeira nota:'))
n2 = float(input('Segunda nota:'))
média = (n1 + n2)/2
print('Tirando {} e {} a média do aluno é {}.'.format(n1,n2,média))
if média >= 5.0 and média < 7:
    print('O aluno está em RECUPERAÇÃO.')
elif média >= 7.0:
    print('O aluno está APROVADO.')
else:
    print('O aluno está REPROVADO.')
#Versão do professor
nota1 = float(input('Primeira nota:'))
nota2 = float(input('Segunda nota:'))
média = (nota1 + nota2)/2
print('Tirando {:.1f} e {:.1f} a média do aluno é {:.1f}.'.format(nota1,nota2,média))
if 7 > média >= 5: #if reduzido
    print('O aluno está em RECUPERAÇÃO.')
elif média < 5:
    print('O aluno está REPROVADO.')
elif média >= 7: #Professor sugere esse elif para deixar o código mais legível.
    print('O aluno está APROVADO.')

