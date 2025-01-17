# Refaça o programa anterior usando funções. A sua função deve receber uma lista e retornar o maior número.

def maior(lista : list):
    maior = lista[0]

    for i in range(len(lista)):
        if lista[i] > maior:
            maior = lista[i]    
    return maior

lista = [99, 98, 100, 105, 200, 347, -2, 45]

meumaior = maior(lista)

print(f"O maior número da lista é o {meumaior}")