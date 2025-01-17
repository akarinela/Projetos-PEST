# Escreva um código em Python que utilize um laço for para imprimir os números de 1 a 15 (inclusive), mas pulando os números 5, 8 e 12.

for a in range(15):
    a += 1
    if a == 5:
        a += 1
    elif a == 8:
        a += 1
    elif a == 12:
        a += 1
    else:
        print(a)