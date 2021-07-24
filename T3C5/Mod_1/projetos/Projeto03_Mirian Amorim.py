
import votacao
import autoriza_voto
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
global idade; 
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

candidatos = { 1:"WillyWonka", 2 :"Bananinha", 3 :"TonhoDaLua", 4 :"Nulo", 5 :"Branco"}
c = f"Digite [1] para {candidatos[1]}\nDigite [2] para {candidatos[2]}\nDigite [3] para {candidatos[3]}\nDigite [4] para {candidatos[4]}\nDigite [5] para {candidatos[5]}"
print(c)
voto = int(input("Faça a sua escolha: "))
votacao(autoriza_voto,voto)
