#1 - Faça um programa que leia o sexo biológico de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
# Caso esteja errado,peça a digitação novamente até ter um valor correto.

sex = str(input('Qual seu sexo ? ').upper())
if sex == "M":
    print('Sexo masculino guardado com sucesso!')
elif sex == "F":
    print('Sexo feminino guardado com sucesso!')
else:
    while not sex == "F" or not sex == "M": 
        print('Sexo digitado não encontrado, digite novamente.')
        sex = str(input('Qual seu sexo ? ').upper())
        if sex == "M":
            print('Sexo masculino guardado com sucesso!')
            break
        elif sex == "F":
            print('Sexo feminino guardado com sucesso!')
            break