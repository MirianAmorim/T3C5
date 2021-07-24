#2 - Faça um programa que leia nome e altura de várias pessoas, guardando tudo em uma lista, depois do dado inserido, pergunte ao usuário se ele quer continuar, se ele não quiser pare o programa. No final mostre:
# Quantas pessoas foram cadastradas
# Mostre a maior altura
# Mostre a menor altura
print('Bem vindo ao cadastro de nome e altura.')
name = []
height = []
form = []
condition = 0
signUp = 0
while condition != "NAO":
    name.append(str(input('Qual seu nome ? ')))
    height.append(float(input('Qual sua altura em centimetros? ').replace("," , ".")))
    signUp += 1
    condition = str(input('Deseja efetuar mais um cadastro ? ').upper().replace("Ã" , "A"))
height.sort()
print(f'Foram cadastradas {signUp} pessoas o mais alto tem {height[-1]}M e o mais baixo tem {height[0]}M')