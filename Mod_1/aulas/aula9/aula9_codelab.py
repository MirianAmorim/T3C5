###Aula 09 - CodeLab - Estruturas de Repetição e Listas
#01 - Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já esteja lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.


# while True:
    
#     entrada = n.append(int(input('Digite um número: ')))
#     if entrada in n:
#         del entrada

#     condicao = str(input('Deseja continuar? SIM ou NÃO? ').upper().replace('Ã', 'A'))
    

#     if condicao == 'NAO':
#         break
# n.sort()
# print(n)
# lista = []


# pergunta = str(input('Deseja continuar ? S/N ').upper())
# while pergunta[0] == 'S':
#     entrada = int(input('Digite o valor: '))
#     pergunta = str(input('Deseja continuar ? S/N ').upper())
#     if entrada in lista:
#         pass
#     else: 
#         lista.append(entrada)
# lista.sort()
# print(lista)




# #02 - Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.
# lista = []
# par = []
# impar = []


# pergunta = str(input('Deseja adicionar um número ? S/N ').upper())
# while pergunta[0] == 'S':
#     entrada = int(input('Digite o valor: '))
#     pergunta = str(input('Deseja continuar ? S/N ').upper())
#     if entrada in lista:
#         pass
#     else: 
#         lista.append(entrada)
#     if entrada % 2 == 0:
#         par.append(entrada)
#     else:
#         impar.append(entrada)
# lista.sort()
# par.sort()
# impar.sort()
# print(lista)
# print(par)
# print(impar)


#Desafio: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.


import random
from random import randint

jogo = []
final = []
var = int(input('Digite a quantidade de jogos'))
for i in range(var):
    while len(jogo) < 6:
        num = randint (1,60)
        if num not in jogo:
            jogo.append(num)
    final.append(jogo)
    jogo.sort()
    print(f'Jogo {i+1}: {jogo}')

    jogo = []

print(jogo)
print(final)