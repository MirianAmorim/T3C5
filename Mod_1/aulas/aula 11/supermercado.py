### Exercício 2- Crie um programa, utilizando dicionário, que simule a baixa de estoque 
# das vendas de um supermercado. Não esqueça de fazer as seguintes validações:​

# Produto Indisponível​
# Produto Inválido​
# Quantidade solicitada não disponível ​

# O programa deverá mostrar para o cliente a quantidade de itens comprados e o total.
carrinho = 0

while True:
    mercadorias = {'Papel-higiênico': 10,'Assolan': 5,'Detergente': 0, 'Desodorante': 3,'Passa-tempo':5, "Parati":3}

    comprados = mercadorias.pop(str(input('Qual produto deseja comprar ?').capitalize()), 'Produto Indisponível')

    if comprados in mercadorias.keys:
        carrinho += 1
    print(comprados)