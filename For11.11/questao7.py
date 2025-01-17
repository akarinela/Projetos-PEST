# Crie um código em Python que calcule a soma dos números primos de 1 a 100 (inclusive) usando o comando for.

soma = 0

for a in range(1,101):
    e_primo = 0
    for i in range(a):
        i += 1
        if a % i == 0:
            e_primo += 1
    if e_primo == 2:
        soma += a

print(soma)

