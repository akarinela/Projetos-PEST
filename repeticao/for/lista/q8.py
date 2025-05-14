# Crie um código em Python que use o comando for para percorrer de 0 até n (inclusive) números e calcule o fatorial de cada número e mostre na tela.

n = int(input('Digite um número: '))

for a in range(n):
    fatorial = 1
    a += 1
    for j in range(a):
        j += 1
        fatorial = fatorial * j
    print(f"O fatorial de {a} é igual a {fatorial}")