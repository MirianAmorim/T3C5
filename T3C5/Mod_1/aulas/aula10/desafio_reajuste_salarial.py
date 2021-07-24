# As empresas @.com resolveram dar um aumento de salário aos seus colaboradores e lhe contrataram para desenvolver o programa que calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5%
# Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.


print ("Bem Vindo!")
print () 

aumento = 0
percentual = 0

faixa1 = 20
faixa2 = 15
faixa3 = 10
faixa4 = 5

salario_atual = float (input ("Para saber qual o valor de seu reajuste e novo salário precisamos que informe seu salário atual: R$").replace(',','.'))

if salario_atual <= 280:
  aumento = salario_atual*(faixa1/100)
  percentual = faixa1
elif salario_atual < 700:
  aumento = salario_atual*(faixa2/100)
  percentual = faixa2
elif salario_atual < 1500:
  aumento = salario_atual*(faixa3/100)
  percentual = faixa3
else: 
  aumento = salario_atual*(faixa4/100)
  percentual = faixa4

salario_reajustado = salario_atual + aumento

print (f"Salário atual: R$ {salario_atual:.2f}")
print (f"Percentual de aumento: {percentual:.2f} %")
print (f"Valor do reajuste: R$ {aumento:.2f}")
print (f"Salário atualizado: R$ {salario_reajustado:.2f}")