# 13. Trocar Metades
# Escreva uma função chamada trocar_metades que troque a primeira metade de uma string
# pela segunda metade e retorne a nova string.
# Exemplo de funcionamento:
# 1 Entrada : trocar_metades (" Pythonista ")
# 2 Sa í da : " istaPython "

def trocar_metades(string: str):
    metade = len(string) // 2
    if len(string) % 2 != 0:
        metade += 1

    return string[metade:] + string[:metade]

print(trocar_metades(' Pythonista '))