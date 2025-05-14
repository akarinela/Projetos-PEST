# 6. Últimos N Caracteres
# Crie uma função chamada ultimos_n que receba uma string e um número inteiro n e retorne
# os últimos n caracteres da string.
# Exemplo de funcionamento:
# 1 Entrada : ultimos_n (" Programar ", 4)
# 2 Sa í da : " amar "

def ultimo_n(string: str, indice: int):
    return string[indice:]

print(ultimo_n('Programar', 4))