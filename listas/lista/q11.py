# Escreva um programa que encontre o maior e o menor número em uma lista de números inteiros. Use um loop for para percorrer a lista.

numeros = [12, 5, 8, 21, 3, 18, 7]
maior = numeros[0]
menor = numeros[0]

for num in numeros:
    if num > maior:
        maior = num
    if num < menor:
        menor = num

print("Maior:", maior)
print("Menor:", menor)