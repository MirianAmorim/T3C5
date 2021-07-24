# Escreva uma função que recebe dois parâmetros e imprime o menor dos dois.
# Se eles forem iguais, imprima que eles são iguais.

def menorValor(n1, n2):
    if n1 == n2:
        return "Os números são iguais."
    else:
        l =[n1, n2]
        l.sort()
        return l[0]

n1 = float(input("Digite um valor: "))
n2 = float(input("Digite outro valor: "))
print(menorValor(n1, n2))