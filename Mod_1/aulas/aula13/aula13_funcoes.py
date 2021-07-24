def area(altura,base):
    calc = altura * base
    print(f'A área do seu terreno é igual a {calc}m²')

print('Vamos calcular a area do seu terreno')
largura = float(input('Qual a altura do seu terreno ?'))
comprimento = float(input('Qual o comprimento ?'))
area(largura,comprimento)