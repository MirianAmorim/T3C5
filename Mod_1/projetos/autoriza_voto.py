
# A 1° Função precisa ser chamada autoriza_voto() ela vai receber como
# parâmetro o ano de nascimento de uma pessoa que será digitado pelo usuário,
# retornando um valor literal indicando se uma pessoa tem voto NEGADO,
# OPCIONAL e OBRIGATÓRIO nas eleições.




def autoriza_voto(i)
    # Condições pra definir a classificação do voto.

    if idade < 16:
        print("Volte ao completar 16 anos.")
        return 
    while idade >=16 and idade <18 or idade >=70:
        print(" Seu voto é FACULTATIVO!")
        opc = input(" Deseja votar? [S] / [N]\n").upper()
        if opc == 'S':
            break
        elif opc == 'N':
            print("SEU VOTO É O SEU FUTURO! SE VOCÊ NÃO ESCOLHER, ESCOLHERÃO POR VOCÊ!")
            break
        else:
            print("Digite uma opção válida: [S] / [N] ")
    else:
        print(" E O SEU VOTO É OBRIGATÓRIO!")
autoriza_voto(idade)
