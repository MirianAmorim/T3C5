#2 – Crie um dicionário em que suas chaves serão os números 1, 4, 5, 6, 7, e 9 (que podem ser armazenados em uma lista) e seus valores correspondentes aos quadrados desses números.
numbers = [1,4,5,6,7,9]
square = dict()

for i in numbers:
    square[i] = i**2
print(square)