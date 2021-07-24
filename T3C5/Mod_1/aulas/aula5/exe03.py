#3 - Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#A) Quantas pessoas tem mais de 18 anos.
#B) Quantos homens foram cadastrados.
#C) Quantas mulheres tem menos de 20 anos.

#variáveis 
man = 0
teenWoman= 0 
try_ = 1
age = 0

var1 = str(input('Qual seu sexo? : ').upper())
var2 = int(input('Qual sua idade ? : ').upper())
var3 = str(input('Deseja continuar ? : ').upper().replace('Ã' , 'A'))
if var2 > 18:
    age += 1
if var1[0] == 'M':
    man += 1
if var1[0] == 'F' and var2 < 20:
    teenWoman += 1
while not var3 == 'NAO':
    var1 = str(input('Qual seu sexo? : ').upper())
    var2 = int(input('Qual sua idade ? : ').upper())
    var3 = str(input('Deseja continuar ? : ').upper().replace('Ã' , 'A'))    
    try_ += 1
    if var2 > 18:
      age += 1
    if var1[0] == 'M':
      man += 1
    if var1[0] == 'F' and var2 < 20:
      teenWoman += 1

print(f'Foram cadastradas {age} pessoa com mais de 18 anos' )
print(f'{man} homens cadastrados')
print(f'{teenWoman} mulheres com menos de 20 anos' )
print(f'Com um total de {try_} pessoas cadastradas')