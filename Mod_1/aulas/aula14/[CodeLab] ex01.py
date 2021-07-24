# 1 - Faça um programa, com uma função que necessite de três argumentos,
# e que forneça a soma desses três argumentos.

def somar(x,y,z):
    return x + y + z

n1 = float(input("Digite um número:"))
n2 = float(input("Digite um número:"))
n3 = float(input("Digite um número:"))
print(somar(n1, n2, n3))