#2 - Escreva um programa que pede a senha uma senha ao usuário, e só sai do loop quando digitarem corretamente a senha. A senha é “Blue123” 
#2b - Exiba quantas vezes o usuário errou a digitação.

key = str(input('Digite a senha: '))
password = "Blue123"
error = 0
while key != password :
    error += 1
    key = str(input('Senha errada!! digite novamente: '))
    if key == password:
        print("Bem vindo(a)")
    elif key == 5:
        print('Tentativas esgotadas')
        break
print(f'Você errou {error} vezes')