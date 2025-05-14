# Primeiros N Caracteres
# Escreva uma função chamada primeiros_n que receba uma string e um número inteiro n e
# retorne os primeiros n caracteres da string.
# Exemplo de funcionamento:
# 1 Entrada: primeiros_n (" Programar " , 5)
# 2 Saída: " Progr "

def primeiro_n(string: str, indice: int):
    return string[:indice]

print(primeiro_n('Programar', 5))