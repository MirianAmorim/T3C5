# 2 - Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’, 
# se seu argumento for positivo, ‘N’, se seu argumento for negativo e ‘0’ se for 0.

def posNeg(n):
    if n > 0:
        return 'P'
    if n < 0:
        return 'N'
    if n == 0:
        return '0'

numero = float(input("Digite um número: "))
print(posNeg(numero))