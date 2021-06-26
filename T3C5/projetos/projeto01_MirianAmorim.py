# Projeto 01 – Detetive
# Esse projeto tem a finalidade de fixar os conhecimentos de Variáveis, Print, Input 
# e Condicionais, para isso crie um programa que faça 5 perguntas para uma 
# pessoa sobre um crime. As perguntas são:
# • "Você telefonou para a vítima?"
# • " Você esteve no local do crime?"
# • " Você mora perto da vítima?"
# • " Você devia para a vítima?"
# • " Você já trabalhou com a vítima?" 
# O programa deve, no final, emitir uma classificação sobre a participação da 
# pessoa no crime.
# Se a pessoa responder positivamente a:
# • 2 questões ela deve ser classificada como "Suspeita",
# • Entre 3 e 4 como "Cúmplice"
# • 5 como "Assassino". 
# • Caso contrário, ele será classificado como "Inocente"

print("\n<<<Inquérito Investigativo>>> \n\n Responda às 5 perguntas a seguir: Sim[S] ou Não[N] ")
print()


cont = 0
a = input("Você telefonou para a vítima? \n").upper()
print()
if a == "S":
    cont += 1
a = input("Você esteve no local do crime? \n").upper()
print()
if a == "S":
    cont += 1
a = input("Você mora perto da vítima? \n").upper()
print()
if a == "S":
    cont += 1
a = input("Você devia para a vítima? \n").upper()
print()
if a == "S":
    cont += 1
a = input("Você já trabalhou com a vítima? \n").upper()
print()
if a == "S":
    cont += 1
if cont <=1:
    print('Você foi considerado "INOCENTE".')
elif cont >= 2 and cont <=4:
    print('Você foi considerado "SUSPEITO".')
else:
    print('Você foi considerado "CULPADO".')

