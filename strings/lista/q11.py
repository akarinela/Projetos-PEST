# 11. String Sem Espaços
# Escreva uma função chamada remover_espacos que remova os espaços do início e do fim de
# uma string usando fatiamento.
# Exemplo de funcionamento:
# 1 Entrada : remover_espacos (" Python ")
# 2 Sa í da : " Python "

def remover_espacos(string: str):
    return string.strip()

print(remover_espacos("   Python "))