# 4. Repetir Palavra
# Crie uma função chamada repetir_palavra que receba uma string e um número inteiro n e
# retorne a string repetida n vezes.
# Exemplo de funcionamento:
# 1 Entrada : repetir_palavra (" Oi " , 3)
# 2 Saída : " OiOiOi "

def repete_palavra(string: str, indice: int):
    return string * indice

entradapalavra = "Oi"
entradanumero = 3
saida = repete_palavra(entradapalavra, entradanumero)
print(saida)