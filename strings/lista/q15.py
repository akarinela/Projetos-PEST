# 15. Letra Central
# Escreva uma função chamada letra_central que receba uma string de tamanho ímpar e
# retorne o caractere central.
# Exemplo de funcionamento:
# 1 Entrada : letra_central (" Python ")
# 2 Sa í da : " h"

def letra_central(string: str):
    meio = len(string) // 2

    return string[meio]

print(letra_central(' Python '))