# Escreva um programa que percorra uma lista de números e crie uma nova lista que contenha apenas os números pares da lista original.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = []

for num in numeros:
    if num % 2 == 0:
        pares.append(num)

print(pares)