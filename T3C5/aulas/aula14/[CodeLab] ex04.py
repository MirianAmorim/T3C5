# 4 -Faça um programa que calcule o salário de um colaborador na empresa XYZ. 
# O salário é pago conforme a quantidade de horas trabalhadas. 
# Quando um funcionário trabalha mais de 40 horas ele recebe um adicional de 1.5 nas horas extras trabalhadas.

def calcSal(sal, horas):
    if horas > 40:
        horasEx = horas - 40
        return ((horasEx * 1.5) + 40) * sal
    elif horas <= 40:
        return horas * sal

salario = float(input("Digite o salário do funcioário: "))
horas = float(input("Digite as horas do funcioário: "))
pagamento = calcSal(salario, horas)
print(f'Este mês, o funcionário receberá R$ {pagamento:.2f}')