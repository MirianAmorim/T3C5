
# A 1° Função precisa ser chamada autoriza_voto() ela vai receber como
# parâmetro o ano de nascimento de uma pessoa que será digitado pelo usuário,
# retornando um valor literal indicando se uma pessoa tem voto NEGADO,
# OPCIONAL e OBRIGATÓRIO nas eleições.




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
