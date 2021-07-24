# A 2° Função será a votacao(), ela vai receber dois parâmetros, autorização (que
# virá da função autoriza_voto()) e o voto que é o número que a pessoa votou.
# Se ela não puder votar, a 2° função terá que retornar “Você não pode votar”,
# caso o contrário a 2° função deve validar o número que a pessoa escolheu

# ela pode escolher de 1 a 5 (crie 3 candidatos para a votação):
# 1, 2 ou 3 - Votos para os respectivos candidatos
# 4- Voto Nulo
# 5 - Voto em Branco

# Sua função votacao() tem que calcular e mostrar:
# O total de votos para cada candidato;
# O total de votos nulos;
# O total de votos em branco;
# Qual candidato venceu a votação.


import autoriza_voto

def votacao(a,v):
    
    
    candidatos = { 1:"WillyWonka", 2 :"Bananinha", 3 :"TonhoDaLua", 4 :"Nulo", 5 :"Branco"}
    # Supostos candidatos (Micheque_Detonautas)
    WillyWonka = 0
    Bananinha = 0
    TonhoDaLua = 0
    Nulos = 0
    Brancos = 0

    # Contagem de votos para cada opção.
    if v == 1:
        WillyWonka += 1     
    elif v == 2:
        Bananinha += 1     
    elif v == 3:
        TonhoDaLua += 1    
    elif v == 4:
        Nulos += 1    
    elif v == 5:
        Brancos += 1        
    else:
        print("Escolha uma opção válida:")
    
    # Verifica se existem mais usuários para votar.    
    continua = input("Próximo!!! (Tem mais alguém pra votar?)").upper() 
    if continua == "S":
        return candidatos
    else:
        # Definindo e mostrando o resultado    
        total_validos = WillyWonka + Bananinha + TonhoDaLua       
        total = WillyWonka + Bananinha + TonhoDaLua + Nulos + Brancos
        print(f"Total de votos:{total}")
        print(f"Total de votos válidos:{total_validos}")
        print(f" O candidato {candidatos[1]} recebeu {WillyWonka} votos.")
        print(f" O candidato {candidatos[2]} recebeu {Bananinha} votos.")
        print(f" O candidato {candidatos[3]} recebeu {TonhoDaLua} votos.")
        print(f" Os votos {candidatos[4]}s receberam o total de {Nulos} votos.")
        print(f" Os votos {candidatos[5]}s receberam o total de {Brancos} votos.")
        return
    
candidatos = { 1:"WillyWonka", 2 :"Bananinha", 3 :"TonhoDaLua", 4 :"Nulo", 5 :"Branco"}
c = f"Digite [1] para {candidatos[1]}\nDigite [2] para {candidatos[2]}\nDigite [3] para {candidatos[3]}\nDigite [4] para {candidatos[4]}\nDigite [5] para {candidatos[5]}"
print(c)
voto = int(input("Faça sua escolha: ")
votacao(autoriza_voto,voto)