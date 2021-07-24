#04 - Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o. Mostre também quantos valores pares foram digitados.
cont = 0
par = 0
for i in range(6):
    num = int(input('Digite o número: '))
    if num % 2 == 0:
        cont += num 
        par += 1
    else:
        pass
print(f'Foram digitados {par} números pares, a soma entre esses números é igual a {cont} ')