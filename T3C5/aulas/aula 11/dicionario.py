#contacts = [('Fulano', '1112-3258'), ('ciclano', '1234-9874'), ('Beltrano', ' 1234-8971'), ('Bartolomeu','1155-6689')]

#phones = dict(contacts)
#nome = str(input('Digite algo'))

#print(phones.get(nome, "olá você errou"))
avengers = {'Chris Evans' : 'Capitão América', 'Mark Ruffalo':'Hulk', 'Tom Hiddleston':'Loki', 'Chris Hemworth':'Thor', 'Scarlett Johansson':'Viúva Negra'}
print(avengers.get('Chris Evans'))
print('Hulk' in avengers.values())
print('Tom Hiddleston' in avengers.keys())
print('Tom Hiddleston' in avengers.keys() or 'Tom Hiddleston' in avengers.values() )
avengers['Jeremy Renner'] = 'Gavião Arqueiro'
print(avengers)
nome =  str(input('Digite o nome do ator '))
personagem = str(input('Digite o nome personagem'))
avengers[nome] = personagem
del avengers['Jeremy Renner']
print(avengers)