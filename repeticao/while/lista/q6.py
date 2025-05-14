# Gere um número aleatório entre 1 e 9 (incluindo 1 e 9). Peça ao usuário para adivinhar o número e diga se o número é 
# muito baixo, muito alto ou se ele acertou. Caso ele digite “sair” o jogo deve acabar.
# OBS: import random e num = random.randint(1,9)

import random
num= random.randint(1,9)

while True:
    num1 = int(input('Digite um número de 1 a 9: '))
    if num1 == num:
        print('Acertou')
        break
    elif num1 < num:
        print('Baixo')
    elif num1 > num:
        print('Alto')