# Crie um código em Python que use o comando for para calcular o valor da somatória dos números inteiros positivos menores que n que são divisíveis por 3 ou 5. Onde n é um número inteiro 
# inserido pelo usuário.

n = int(input('Digite um número: '))

soma = 0

for numero in range(n):
    if numero % 3 == 0 or numero % 5 == 0:
        soma += numero

print(soma)