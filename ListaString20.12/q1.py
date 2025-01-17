# Função de Primeira e Última Letra
# Enunciado: Desenvolva uma função chamada primeiro_e_ultimo que recebe uma palavra e retorna a primeira e a última letra dela.
# Exemplo:
# Entrada: "Python"
# Saída: "Pn"

def primeiro_e_ultimo(string: str):
    primeira = string[0]
    tamanho = len(string)
    ultimo = string[tamanho -1]
    novastring = primeira + ultimo
    return novastring

print(primeiro_e_ultimo('Python'))