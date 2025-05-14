# 10. Palíndromo Simples
# Crie uma função chamada palindromo_simples que verifique se uma string é igual à sua
# reversa. Retorne True ou False.
# Exemplo de funcionamento:
# 1 Entrada : palindromo_simples (" arara ")
# 2 Sa í da : True

def palindromo_simples(string: str):
    return string == string [::-1]

print(palindromo_simples('arara'))