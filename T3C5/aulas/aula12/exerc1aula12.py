# aluno = {}
# nome = input('Digite o nome do aluno ').title()
# media =  float(input('Digite a média do aluno'))
# aluno[nome] = media
# for i in aluno:
#     print(aluno.get(i))
# if media > 5 and media < 6.9:
#     print('Aluno em recuperação!')
# elif media < 5:
#     print('Aluno reprovado!')
# else:
#     print('Aluno aprovado!')
infos = {}
nome = input("Digite o nome do sujeito")
anodnasc = int(input('Digite o ano de nascimento do sujeito'))
ctdb = int(input('Digite a carteira de trabalho'))
infos[nome] = [anodnasc,ctdb]
print(infos)
# for i in infos:
if ctdb != 0:
    ctt = int(input('Digite o ano da contratação '))
    sal = input('Digite o salario')
    infos[nome]=[anodnasc, ctdb, ctt, sal]
    aposentadoria = ctt + 35 - anodnasc
    print(infos)
    print(aposentadoria)