# 14. Inverter Metade Direita
# Crie uma função chamada inverter_direita que receba uma string e inverta apenas a segunda
# metade dela.
# Exemplo de funcionamento:
# 1 Entrada : inverter_direita (" Pythonista ")
# 2 Sa í da : " Pythontsni "

def inverter_direita(string: str):
    metade = len(string) // 2
    primeira_metade = string[:metade]
    segunda_metade = string[metade:][::-1]

    return primeira_metade + segunda_metade

print(inverter_direita(' Pythonista '))