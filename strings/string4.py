# 4 - Leia uma string do usuário e mostre essa string caracter-a-caratere (um caractere por linha) usando for
# 1a maneira

str = input('Digite algo: ')
for indice in range(0, len(str), 1):
    print(str[indice])

# 2a maneira

str = input('Digite algo: ')
for item in str:
    print(item)