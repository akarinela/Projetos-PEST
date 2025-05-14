# 8. Caracteres Intercalados
# Crie uma função chamada intercalados que receba uma string e retorne apenas os caracteres
# nas posições pares da string.
# Exemplo de funcionamento:
# 1 Entrada : intercalados (" abcdef ")
# 2 Sa í da : " ace "

def intercalados(string: str):
    return string[::2]

print(intercalados('abcdef'))