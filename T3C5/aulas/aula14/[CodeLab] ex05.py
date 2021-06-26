# 5 - Faça um programa que calcule através de uma função o IMC de uma pessoa que tenha 1,68 e pese 75kg.

def imcCalc(altura, peso):
    return peso/altura/altura

altura = float(input("Altura (m): ").replace(",","."))
peso = float(input("Peso (Kg): ").replace(",","."))
print(f"IMC: {imcCalc(altura, peso):.2f}")