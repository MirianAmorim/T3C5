#01 - Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso. (utilizar while sem break)

number1 = float(input('Digite um número: ').replace(',','.'))
number2 = float(input('Digite outro número: ').replace(',','.'))
print('Escolha uma das opções do menu a baixo')
print('[1] para somar os dois números') 
print('[2] para multiplicar')
print('[3] para sabe qual é o maior entre eles')
print('[4] para digitar novos números')
print('[5] para sair do programa')   
select = float(input('Qual opção deseja ?: ').replace(',','.'))

while select != 5:
    if select == 0 or select > 5:
        print('Opção invalida tente novamente')
        number1 = float(input('Digite um número: ').replace(',','.'))
        number2 = float(input('Digite outro número: ').replace(',','.'))
        print('Escolha uma das opções do menu a baixo')
        print('[1] para somar os dois números') 
        print('[2] para multiplicar')
        print('[3] para sabe qual é o maior entre eles')
        print('[4] para digitar novos números')
        print('[5] para sair do programa')   
        select = float(input('Qual opção deseja ?: ').replace(',','.'))
    elif select == 1:
        print(f'A soma entre {number1} e {number2} é igual á {number1 + number2:.2f}')
        print('Escolha uma das opções do menu a baixo')
        print('[1] para somar os dois números') 
        print('[2] para multiplicar')
        print('[3] para sabe qual é o maior entre eles')
        print('[4] para digitar novos números')
        print('[5] para sair do programa')   
        select = float(input('Qual opção deseja ?: ').replace(',','.'))
    elif select == 2:
        print(f'{number1} X {number2} = {number1*number2:.2f}')
        print('Escolha uma das opções do menu a baixo')
        print('[1] para somar os dois números') 
        print('[2] para multiplicar')
        print('[3] para sabe qual é o maior entre eles')
        print('[4] para digitar novos números')
        print('[5] para sair do programa')   
        select = float(input('Qual opção deseja ?: ').replace(',','.'))
    elif select == 3:
        if number1 > number2:
            print(f'O número {number1} é maior')
        elif number2 > number1:
            print(f'O número {number2} é maior')
        elif number2 == number1:
            print('Os dois números são iguais')
        print('Escolha uma das opções do menu a baixo')
        print('[1] para somar os dois números') 
        print('[2] para multiplicar')
        print('[3] para sabe qual é o maior entre eles')
        print('[4] para digitar novos números')
        print('[5] para sair do programa')   
        select = float(input('Qual opção deseja ?: ').replace(',','.'))
    elif select == 4:
        number1 = float(input('Digite um número: ').replace(',','.'))
        number2 = float(input('Digite outro número: ').replace(',','.'))
        print('Escolha uma das opções do menu a baixo')
        print('[1] para somar os dois números') 
        print('[2] para multiplicar')
        print('[3] para sabe qual é o maior entre eles')
        print('[4] para digitar novos números')
        print('[5] para sair do programa')   
        select = float(input('Qual opção deseja ?: ').replace(',','.'))
print('O programa foi encerrado')