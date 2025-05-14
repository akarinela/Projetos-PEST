# Defina uma função chamada contagem_regressiva que aceita um número inteiro positivo como parâmetro e imprime uma contagem regressiva a partir desse número até zero.

numero = int(input('Digite um número inteiro: '))

def contagem_regressiva(numero):
    while numero >= 0:
        print(numero)
        numero -= 1

contagem_regressiva(numero)