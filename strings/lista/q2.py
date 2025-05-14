# Substring por Índices
# Enunciado: Faça uma função chamada intervalo que receba uma palavra e dois números. A função deve devolver a parte da palavra entre esses números.
# Exemplo:
# Entrada: "Python", 1, 4
# Saída: "yth"

def intervalo(string: str, indice1: int, indice2: int):
    return string[indice1 : indice2]

print(intervalo('Python', 1, 4))