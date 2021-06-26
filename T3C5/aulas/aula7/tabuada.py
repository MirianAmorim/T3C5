#02 - Crie um programa que pergunte ao usuário um número inteiro e faça a tabuada desse número.
num = int(input('Digite um número: '))
for i in range(1,11):
    print(f"{i} x {num} = {i * num}")