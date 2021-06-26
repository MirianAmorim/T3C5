#4 - Crie um jogo onde o computador vai “pensar” em um número entre 0 e 10. O jogador vai tentar adivinhar qual número foi escolhido até acertar, mostrando no final quantos palpites foram necessários para vencer.
import random 

result = random.randint(0,10)
user = int(input('O programa vai pensar em um número de 0 a 10\nTente adivinhar este número\nResposta: '))
try_ = 1

while not result == user:
  print('Infelizmente você errou')
  user = int(input('Tente novamente\nResposta: '))
  try_ += 1
if result == user:
  print('Parabéns! Você acertou!')
print(f'Você tentou {try_} vezes')