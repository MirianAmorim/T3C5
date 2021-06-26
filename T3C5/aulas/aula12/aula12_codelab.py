#Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela. A média para aprovação é 7. Se o aluno tirar entre 5 e 6.9 está de recuperação, caso contrário é reprovado.
alunos = {}
nota = []


nome = str(input('Qual seu nome'))

for i in range(3):
    notas = float(input('Qual foi sua nota').replace(',','.'))
    nota.append(notas)
    alunos[nome] = notas
soma = sum(nota)
media = soma/3

if soma > 5 and soma < 6.9:
    print(f'{media} Recuperação ')
elif soma >= 7 :
    print(f' {media}Aprovado')
else:
    print(f' {media}reprovado')
alunos[nome] = nota 
print(alunos)


#Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastros (com idade) em um dicionário. 
# Se por acaso a CTPS for diferente de 0, o dicionário receberá também o ano de contratação e o salário. 
# Calcule e acrescente , além da idade  , com quantos anos a pessoa vai se aposentar. 
# Considere que o trabalhador deve contribuir por 35 anos para se aposentar.
dicionario = {}
condição = 0
while condição != 'NAO':
    nome = str(input('Qual seu nome' ))
    ano = int(input('Em qual ano você nasceu ?' ))
    Carteira = int(input('Qual número da carteira de trabalho ? '))
    idade = 2021 - ano
    dicionario[nome] = ano, idade
    if Carteira != 0:
        contratação = int(input('Qual ano de contratação ? '))
        salario = float(input('Qual é o salário ?'))
        aposentar = (contratação + 35) - ano
    dicionario[nome] = salario, aposentar, idade, salario, aposentar
condição = str(input('Deseja cadastrar mais um usuário ?').upper().replace(' ','').replace('Ã','A'))


print(dicionario)

# DESAFIO: Crie um programa que leia nome, sexo biologico e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma
# lista. No final, mostre:
# A) Quantas pessoas estão cadastradas.
# B) A média da idade.
# C) Uma lista com as mulheres.
# D) Uma lista com as idades que estão acima da média.
# OBS: O programa deve garantir que o sexo digitado seja válido, e que quando
# perguntar ao usuário se deseja continuar a resposta seja somente sim ou não.
nome = 0
sexo = 0
idade = 0
pessoa = 0
mediaIdade = 0  
mulheres =  0
while condição != 'NAO':
    nome = str(input('Qual seu nome ' ).title().strip())
    sexo = str(input('Qual seu sexo biológico ? ' ).strip().capitalize())
    while sexo != 'Maculino' or sexo != 'Feminino':
        sexo = str(input('Qual seu sexo biológico ? ' ).strip().capitalize())
    idade = int(input('Qual é sua idade ? '))
    condição = str(input('Deseja cadastrar mais um usuário ?').upper().replace(' ','').replace('Ã','A'))
  
# 3.	DESAFIO: Crie um programa que leia nome, sexo e idade de várias pessoas, 
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
# A) Quantas pessoas estão cadastradas.
# B) A média da idade.
# C) Uma lista com as mulheres.
# D) Uma lista com as idades que estão acima da média.
# OBS: O programa deve garantir que o sexo digitado seja válido, 
# e que quando perguntar ao usuário se deseja continuar a resposta seja somente sim ou não.
lista = []
nome = 0
sexo = 0
idades = []
pessoas = 0
quantidade_F =[]
idade_acima_media = []
media_idade=[]
cadastro=0
while cadastro != 'Não':
    pessoas +=1
    dicionario = {}
    nome=input('Qual é o seu nome?\n').title().strip()
    sexo=input('Qual é o seu sexo? Masculino ou Feminino:\n').capitalize().strip()
    while sexo != 'Masculino' and sexo != 'Feminino':
        sexo=input('Qual é o seu sexo? Masculino ou Feminino:\n').capitalize().strip()
    if sexo == 'Feminino':
        quantidade_F.append(nome)
    idade=int(input('Qual é a sua idade?\n'))
    cadastro = input('Deseja cadastrar outra pessoa?:\n').capitalize().replace('a','ã').replace(' ','')
    dicionario[nome] = sexo, idade
    idades.append(idade)
    lista.append(dicionario)
soma_idade=sum(idades)
media_idade= soma_idade/pessoas
for i in idades:
    if i > media_idade:
        idade_acima_media.append(i)

print()
print(f'Minha lista {lista}')
print()
print(f'As mulheres são {quantidade_F}')
print()
print(f'{idade_acima_media}São as idades que estão acima da media')
print()
print(f'A media de idades é de {media_idade}')
  
# 4.	 Desafio: Continuando o exercício 3 crie agora um boletim escolar, 
# seu programa deve receber 5 notas de 15 alunos, assim como o nome desses alunos, 
# o programa tem que calcular a média desse aluno e mostrar a situação dele, seguindo 
# os mesmos critérios apresentados no exercício 3. No final apresente todos nomes, as 
# 5 notas, as médias e as situações dos 15 alunos de uma vez só.
alunos = {}
for i in range(2):
    nome=input('Qual é o seu nome?\n')
    lista_notas=[]
    soma=0
    for u in range(5):
        nota=float(input('Digite a sua nota:\n'))
        lista_notas.append(nota)
        soma=sum(lista_notas)
        media=soma/5
    situacao= 0
    if media > 5 and media <= 6.9:
        situacao='Recuparação'
    elif media >= 7:
        situacao='Aprovado'
    else:
        situacao='Reprovado'
    alunos[nome]= lista_notas, media,situacao
print(alunos)