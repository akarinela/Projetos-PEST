# Crie um programa para verificar se um número é primo ou não. Utilize o comando for.

numero = int(input('Digite um número: '))
e_primo = 0

for a in range(numero):
    a += 1
    if numero % a == 0:
        e_primo += 1

if e_primo == 2:
    print("O número é primo")
else:
    print("O numero não é primo")