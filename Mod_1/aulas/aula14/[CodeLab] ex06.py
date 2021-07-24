# Escreva uma função que, dado um número nota representando a nota de um estudante, 
# converte o valor de nota para um conceito (A, B, C, D, E e F).
# Nota	Conceito
# >=9.0	A
# >=8.0	B
# >=7.0	C
# >=6.0	D
# >=5.0 E**
# <=4.0	F

def nConceito(nota):
    if nota >= 9.0:
        return 'A'
    elif nota >= 8.0:
        return 'B'
    elif nota >= 7.0:
        return 'C'
    elif nota >= 6.0:
        return 'D'
    elif 4.0 < nota <= 6.0:
        return 'E'
    elif nota <= 4.0:
        return 'F'

nota = float(input('Insira a Nota:').replace(",","."))
print(f'Nota conceito: {nConceito(nota)}')