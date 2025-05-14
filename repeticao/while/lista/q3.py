# Crie um código em Python que use o comando "while" para ler números inteiros inseridos pelo usuário até que o número inserido seja zero e imprima a soma de todos os números inseridos.

contadora = 1
soma = 0

while True:
    numero = int(input('Digite um número: '))
    soma += numero
    contadora = contadora + 1
    if numero == 0:
        print(soma)   
        break