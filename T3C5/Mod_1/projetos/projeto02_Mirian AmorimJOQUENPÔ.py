# Utilizando os conceitos aprendidos até estruturas de repetição, crie um programa que jogue pedra, papel e tesoura (Jokenpô) com você.
# O programa tem que:
# • Permitir que eu decida quantas rodadas iremos fazer;
# • Ler a minha escolha (Pedra, papel ou tesoura);
# • Decidir de forma aleatória a decisão do computador;
# • Mostrar quantas rodadas cada jogador ganhou;
# • Determinar quem foi o grande campeão de acordo com a quantidade de 
# vitórias de cada um (computador e jogador);
# • Perguntar se o Jogador quer jogar novamente, se sim inicie volte a escolha 
# de quantidade de rodadas, se não finalize o programa.

from random import randint


print()
print("<<<<<BEM VINDO AO JOGO>>>>>")
print("            JO\n           QUEN\n            PÔ...")
opcoes = ["PEDRA", "PAPEL", "TESOURA"]


while True: # Faz a repetição do código todo.
    contador = 0  # Refere a quantidade de jogos escolhida.
    empate = 0
    vitoriapc = 0
    vitoriajogador = 0
    print()
    x = int(input("Digite quantas vezes quer jogar: "))
    print()
    print(f"Muito bem! Jogaremos {x}X!")
    print()
    
    

    while contador != x : # Repete enquanto a quantidade jogos escolhida não acontecer.
        print("ESSAS SÃO AS SUAS OPÇÕES: \n (0)PEDRA \n (1)PAPEL \n (2)TESOURA")
        print()
        jogador = int(input("Escolha uma delas: [0]Pedra, [1]papel ou [2]tesoura? "))
        
        while jogador != 0 and jogador != 1 and jogador != 2:
            print("Escolha uma opção válida!")
            jogador = int(input("Escolha uma delas: [0]Pedra, [1]papel ou [2]tesoura? "))

        print()
        print(f"Você escolheu {opcoes[jogador]}.") # Lê o valor dentro da lista, caso contrário leria somente o indice.
        pc = randint(0,2)
        print(f"O computador escolheu {opcoes[pc]}.")
        if jogador == 0 and pc == 2 or jogador == 1 and pc == 0 or jogador == 2 and pc == 1: 
            print("VOCÊ GANHOU!")
            print("-----------//-----------")
            print()
            vitoriajogador += 1
        elif jogador == 2 and pc == 0 or jogador == 0 and pc == 1 or jogador == 1 and pc == 2:
            print("O COMPUTADOR GANHOU!")
            print("-----------//-----------")
            print()
            vitoriapc += 1
        else:
            print("VOCÊS EMPATARAM!")
            print("-----------//-----------")
            print()
            empate += 1
        contador += 1


    if vitoriajogador > vitoriapc:
        print(f"<<<<PARABÉN! VOCÊ FOI O GANHADOR FINAL, COM {vitoriajogador} VITÓRIA(S) E {empate} EMPATE(S)>>>>")
        print()
    elif vitoriajogador == vitoriapc:
        print("  \U0001F614")
        print("EMPATE")
        print()  
    else:
        print(f"O COMPUTADOR GANHOU, COM {vitoriapc} VITÓRIA(S) E {empate} EMPATE(S)\n              É HORA DA \n             REVANCHE!!!")
        print()

    resp = input("Quer jogar novamente? [S] / [N] ").upper()
    if resp != 'S': # Condição final para verificar se repete ou não.
        break