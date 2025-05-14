# Crie um programa para converter de binário para decimal usando while.

binario = int(input('DIgite um número em binário: '))
expoente = 0
decimal = 0

while binario > 0:
    dig = binario %10
    decimal += dig * 2 ** expoente
    expoente += 1
    binario = binario //10

print(decimal)