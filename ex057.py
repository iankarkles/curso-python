#Exercício 57 - Versão do Ian - Obs.: depois de muito rematar num exercício simples, notei que o problema estava no Upper e Strip dentro dos parênteses.
sexo = str(input('Informe seu sexo: [M/F]')).upper().strip()
while sexo != 'M' and sexo !='F':
   sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).upper().strip()
print(f'Sexo {sexo} registrado com sucesso') 

#Versão do professor

sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos, Por favor, informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))
