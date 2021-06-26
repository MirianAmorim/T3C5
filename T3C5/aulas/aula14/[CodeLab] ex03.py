# 3 - Faça um programa com uma função chamada somaImposto.
# A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre 
# vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto. 
# A função “altera” o valor de custo para incluir o imposto sobre vendas.

def somaImposto(taxaImposto, custo):
    return custo*(taxaImposto/100 +1)

price = float(input('Digite o custo do produto: '))
imposto = float(input('Digite o imposto do produto (%): '))
newPrice = somaImposto(imposto, price)
print(f'O preço do produto com imposto será R$ {newPrice:.2f}')