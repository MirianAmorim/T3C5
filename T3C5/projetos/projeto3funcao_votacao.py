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
def autoriza_voto():
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
        print(" Ainda não pode votar. Volte ao completar 16 anos.")
    elif idade >=16 and idade <18 or idade >=70:
        print(" E seu voto é FACULTATIVO!")
    else:
        print(" E O SEU VOTO É OBRIGATÓRIO!")

autoriza_voto()

def votacao(autorizacao,voto):
    
    autorizacao = autoriza_voto()
    if idade < 16:
        print("<<<<<VOCÊ NÃO PODE VOTAR>>>>>")
    else:
        candidatos = {"Candidato_1": 0,"Candidato_2": 0,"Candidato_3": 0,"Branco": 0,"Nulo": 0}
        for i in candidatos:
            print(i)
    voto = 
votacao()