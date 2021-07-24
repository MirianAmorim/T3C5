# DESAFIO -  Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA 
# e devolva uma string no formato D de mesPorExtenso de AAAA. Opcionalmente, valide a data e retorne NULL 
# caso a data seja inválida. Considere que Fevereiro tem 28 dias e que a cada 4 anos temos ano bisexto, 
# sendo que nesses casos Fevereiro terá 29 dias.
 
import calendar
cal = calendar.Calendar()
def validaData(data):
    if data[0] in cal.itermonthdays(data[2],data[1]):
        return True
    else: return False

def mesExtenso(data):                             
        return calendar.month_name[data[1]]

mesPT_BR = {"January": "Janeiro", "February": "Fevereiro", "March":"Março", "April":"Abril", "May":"Maio",
             "June":"Junho", "July":"Julho", "August":"Agosto", "September":"Setembro", "October":"Outubro",
             "November":"Novembro", "December":"Dezembro"} 
while True:
    data_str = input("Digite uma data: (DD/MM/YYYY) ").split("/")
    if len(data_str[0]) > 0 and len(data_str[1]) > 0 and len(data_str[2]) > 0:
        data = [int(data_str[0]), int(data_str[1]), int(data_str[2])]
        break
    else:
        print("Tente novamente!") 
        continue

if validaData(data) == True:
    print(f"São Paulo, {data[0]} de {mesPT_BR[mesExtenso(data)]} de {data[2]}.")
else: print("NULL")


