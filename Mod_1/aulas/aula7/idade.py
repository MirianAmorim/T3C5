#03 - Crie um programa que leia o ano de nascimento de sete pessoas. No final,mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
adult = 0
teen = 0
for i in range(7):
   age = int(input('Digite sua idade: '))
   if age >= 18:
         adult += 1
   if age < 18:
          teen += 1
print(f'Dos 7 participantes {teen} tem menos de 18 anos e {adult} Já atingiram a maioridade.')