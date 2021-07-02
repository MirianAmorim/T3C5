while True:
    # importa a localização atual e a biblioteca data e tempo.
    import locale
    from datetime import datetime
    locale.setlocale(locale.LC_TIME, 'pt_BR.utf8')
    
    # Pede ao usuário a data de nascimento e configura o formato.
    data_nascimento = input("Digite sua data de nascimento:\n ")
    data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y").date()
    
    
    # Puxa a data atual.
    hoje = datetime.today().date()
    
    # Faz os cálculos da idade do usuário.
    idade = hoje.year - data_nascimento.year
    confirma_mes = hoje.month - data_nascimento.month
    confirma_dia = hoje.day - data_nascimento.day
    
    # Transforma tudo em inteiro.
    idade = int(idade)
    confirma_mes = int(confirma_mes)
    confirma_dia = int(confirma_dia)

    # Condições
    if confirma_mes < 0 :
        idade = idade -1
    elif confirma_dia < 0 and confirma_mes == 0:
        idade = idade -1
    print(f"Você tem {idade} anos.")
    if idade < 16:
        print("Volte ao completar 16 anos.")
    elif idade >=16 and idade <18 or idade >=70:
        print(" E seu voto é FACULTATIVO!")
    else:
        print(" E O SEU VOTO É OBRIGATÓRIO!")




    if idade < 16:
        print(" Ainda não pode votar!")
    elif idade >=16 and idade <18 or idade >=70:
        opc = (" Seu voto é opcional \n Deseja votar? [S] / [N]\n")
        if opc == 'S':
            pass
        elif opc == 'N':
            print("SEU VOTO É O SEU FUTURO! SE VOCÊ NÃO ESCOLHER, ESCOLHERÃO POR VOCÊ!")
        else:
            print("Digite uma opção válida: [S] / [N] ")
    else:
        # Supostos candidatos (Micheque_Detonautas)
        WillyWonka = 0
        Bananinha = 0
        TonhoDaLua = 0
        Nulos = 0
        Brancos = 0
        
        candidatos = ["WillyWonka","Bananinha","TonhoDaLua","Nulo","Branco"]
        
        print()
        print(f"Digite [1] para {candidatos[:1]}\nDigite [2] para {candidatos[1:2]}\nDigite [3] para {candidatos[2:3]}\nDigite [4] para {candidatos[3:4]}\nDigite [5] para {candidatos[4:5]}")
        print()       
        voto = int(input(f"Faça sua escolha: "))
        
        if voto == 1:
            WillyWonka += 1     
        elif voto == 2:
            Bananinha += 1     
        elif voto == 3:
            TonhoDaLua += 1    
        elif voto == 4:
            Nulos += 1    
        elif voto == 5:
            Brancos += 1        
        else:
            print("Escolha uma opção válida:")
        resp = input("Tem mais alguém pra votar?").upper()
        if 'S' not in resp:
            break
            
total_votantes =  WillyWonka + Bananinha + TonhoDaLua + Nulos + Brancos  
print(total_votantes)
total_votos_validos = WillyWonka + Bananinha + TonhoDaLua
print(total_votos_validos)
    # print(f" O candidato {candidatos[:1]} recebeu {(WillyWonka)} votos.)
    # print(f" O candidato {candidatos[1:2]} recebeu {Bananinha} votos.)
    # print(f" O candidato {candidatos[2:3]} recebeu {TonhoDaLua} votos.)
    # print(f" O candidato {candidatos[3:4]} recebeu {Nulos} votos.)
    # print(f" O candidato {candidatos[4:5]} recebeu {Brancos} votos.)      

           
