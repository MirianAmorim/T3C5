# importa a localização e a biblioteca data e tempo.
import locale
from datetime import datetime
locale.setlocale(locale.LC_TIME, 'pt_BR.utf8')

def autoriza_voto(idade):
        # tratamento data p/ verificar o idade.
    if idade < 16:
        print("Volte ao completar 16 anos.") 
        print()
        return False
    elif idade >=16 and idade <18 or idade >=70:
        print(" Seu voto é FACULTATIVO!")
        print()
        opc = input(" Deseja votar? [S] / [N]\n").upper()
        if opc == 'S':  
            return True
        elif opc == 'N':
            print("SEU VOTO É O SEU FUTURO! SE VOCÊ NÃO ESCOLHER, ESCOLHERÃO POR VOCÊ!") 
            print()
            return False
    elif idade >= 18 and idade < 70:
        print(" E O SEU VOTO É OBRIGATÓRIO!") 
        print()
        return True

def votacao(a,v):
    # Contagem de votos para cada opção.
    
    if a == True:
        if v == 1:
            votos[1] += 1   
        elif v == 2:
            votos[2] += 1     
        elif v == 3:
            votos[3] += 1    
        elif v == 4:
            votos[4] += 1    
        elif v == 5:
            votos[5] += 1        
        else:
            return 
    else: 
        print('<<<VOTO NÃO COMPUTADO>>>')
        print()    
    
            
# inicializa votos dos candidatos
votos = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
 
while True:
        
    # Pede ao usuário a data de nascimento e configura o formato.
    data_nascimento = input("Digite sua data de nascimento:\n ")
    data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y").date()
    # Puxa a data atual para comparação.
    hoje = datetime.today().date()
    # Faz os cálculos da idade do usuário. 
    idade = hoje.year - data_nascimento.year
    confirma_mes = hoje.month - data_nascimento.month
    confirma_dia = hoje.day - data_nascimento.day
    # Transforma tudo em inteiro.
    idade = int(idade)
    confirma_mes = int(confirma_mes)
    confirma_dia = int(confirma_dia)
    # Condições pra definir se o usuário ja completou o ano.
    if confirma_mes < 0 :
        idade = idade -1
    elif confirma_dia < 0 and confirma_mes == 0:
        idade = idade -1
    print(f"Você tem {idade} anos.")
    
    aut = autoriza_voto(idade)
    candidatos = { 1:"WillyWonka", 2 :"Bananinha", 3 :"TonhoDaLua", 4 :"Nulo", 5 :"Branco"}
    print(f"Digite [1] para {candidatos[1]}\nDigite [2] para {candidatos[2]}\nDigite [3] para {candidatos[3]}\nDigite [4] para {candidatos[4]}\nDigite [5] para {candidatos[5]}")
    print()
    voto = int(input("Faça a sua escolha: "))
    print()
    
    # Chamando as funções. 
    votacao(aut,voto)
    
    # Verifica se existem mais usuários para votar.    
    continua = input("Próximo!!! (Tem mais alguém pra votar?)").upper() 
    print()
    if continua == "S":
        continue
    elif continua != "S":
        break    
        
# Mostrando o resultado    
print(f"Total de votos:{votos[1] + votos[2] + votos[3] + votos[4] + votos[5]}")
print(f"Total de votos válidos:{votos[1] + votos[2] + votos[3]}")
print(f" O candidato {candidatos[1]} recebeu {votos[1]} votos.")
print(f" O candidato {candidatos[2]} recebeu {votos[2]} votos.")
print(f" O candidato {candidatos[3]} recebeu {votos[3]} votos.")
print(f" Os votos {candidatos[4]}s receberam o total de {votos[4]} votos.")
print(f" Os votos {candidatos[5]}s receberam o total de {votos[5]} votos.")    