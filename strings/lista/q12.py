# 12. Duplicar Primeira Metade
# Crie uma função chamada duplicar_metade que receba uma string e retorne a primeira metade
# da string duplicada.
# Exemplo de funcionamento:
# 1 Entrada : duplicar_metade (" Programar ")
# 2 Sa í da : " ProPro "

def duplicar_metade(string: str):
    metade = len(string) // 2
    return string[:metade] * 2

print(duplicar_metade('Programar'))