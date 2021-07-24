#01 - Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
heavy = 0
light = 100000000
user = 0 
assistant = 0
for i in range(5):
    user = float(input('qual peso ?').replace(',','.'))
    if user > heavy:
        heavy = user
    if user < light:
        light = user

    
print(f'O maior peso foi {heavy} e o menor peso foi {light}')