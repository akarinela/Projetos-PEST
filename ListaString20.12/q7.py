# 7. Substituir Primeira Letra
# Escreva uma função chamada trocar_primeira_letra que receba uma string e substitua o
# primeiro caractere por um #.
# Exemplo de funcionamento:
# 1 Entrada : trocar_primeira_letra (" Python ")
# 2 Sa í da : "# ython "

def trocar_primeira_letra(string: str):
    return "#" + string[1:]

print(trocar_primeira_letra("Python"))