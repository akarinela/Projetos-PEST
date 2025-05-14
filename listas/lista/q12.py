# Refaça o programa anterior usando funções. A sua função deve receber uma lista e retornar outra lista com duas posições, sendo a primeira posição o menor número e a segunda o maior.

def encontrar_extremos(lista):
    menor = lista[0]
    maior = lista[0]
    for num in lista:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    return [menor, maior]

numeros = [12, 5, 8, 21, 3, 18, 7]
resultado = encontrar_extremos(numeros)
print(resultado)