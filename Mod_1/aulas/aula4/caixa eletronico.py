#Caixa eletrônico

# Faça um Programa para um caixa eletrônico. O programa deve perguntar ao usuário a valor do saque e depois informar as notas de cada valor serão fornecidos. As notas disponíveis serão de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.

#Exemplo 1: Para sacar a quantia de 256 reais, o programa oferece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;

#Exemplo 2: Para sacar a quantia de 399 reais, o programa oferece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.
# Código para facil manutenção
print ( 'Qual a quantidade deseja sacar?' )
saque  =  int ( input ( 'R $' ))
# variáveis ​​para a quantiade de notas 
quant1  =  0
quant2  =  0
quant3  =  0
quant4  =  0
quant5  =  0
# varáveis ​​para o valor das notas
valor1  =  100 
valor2  =  50
valor3  =  10
valor4  =  5
valor 5  =  1
# Repetição caso o usuário digite um valor incorreto
enquanto  saque  <  10  ou  saque  >  600 :
    imprimir ( 'Quantidade informada inválida, digite novamente' )
    saque  =  int ( input ( 'R $' ))
#aux <- é uma variável que ajuda a não perder o valor que o usuário digitou.
aux  =  saque 
# começando das notas maiores para as menores fazendo a divisão inteira do valor do usuário, depois diminuindo ele pela quantidade de notas multiplicados pelo valor da nota.
quant1  =  aux  //  valor1
aux  =  aux  - ( quant1 * valor1 )
#assim no próximo calculo o valor de aux é igual ao que restou do primeiro calculo. 
quant2  =  aux  //  valor2
aux  =  aux  - ( quant2 * valor2 )

quant3  =  aux  //  valor3
aux  =  aux  - ( quant3 * valor3 )

quant4  =  aux  //  valor4
aux  =  aux  - ( quant4 * valor4 )

quant5  =  aux  //  valor5
aux  =  aux  - ( quant5 * valor5 )

print ( f'Para sacar a quantia de R $ { saque } , você vai precisar de: ' )
#Se a quantidade de notas principais menores que 1, o usuário não vai ver o imprimir referente a ela.
se  quant1  >  0 :
    imprimir ( f ' { quant1 } notas de R $ { valor1 } ' )
se  quant2  >  0 :
    imprimir ( f ' { quant2 } notas de R $ { valor2 } ' )
se  quant3  >  0 :
    imprimir ( f ' { quant3 } notas de R $ { valor3 } ' )
se  quant4  >  0 :
    imprimir ( f ' { quant4 } notas de R $ { valor4 } ' )
se  quant5  >  0 :
    imprimir ( f ' { quant5 } notas de R $ { valor5 } ' )