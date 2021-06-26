#1 - Crie uma lista composta que recebe 5 nomes e 5 idades de clientes, utilizando o for e o if, verifique quais clientes são maiores de idade e quais são menores de idade e mostre na tela a seguinte frase para cada um deles: 'Fulano é maior de idade' ou 'Fulana é menor de idade' e também quantos são maiores e quantos são menores de idade
users = []
adults = 0
teens = 0
for signUp in range(5):
    name = []
    age = []
    name.append(str(input('Qual seu nome ? ')))
    age.append(int(input('Qual sua idade? ')))
    users.append(name + age)
for i in users:
    if i[1] >= 18:
        print(f'{i[0]} é maior de idade!')
        adults += 1
    else:
        print(f'{i[0]} é menor de idade!')
        teens += 1
print(f'exitem {adults} maiores e {teens} menores')