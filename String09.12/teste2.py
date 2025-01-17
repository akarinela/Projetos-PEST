# Indexação de strings
str = 'caneta'

print(f'Primeira letra: {str[0]}')
print(f'Segunda letra: {str[1]}')
print(f'Terceira letra: {str[2]}')
print(f'Quarta letra: {str[3]}')
print(f'Quinta letra: {str[4]}')
print(f'Sexta letra: {str[5]}')
# print(str[6]) - ERRO

# Acessando elementos (Segunda maneira)
str = 'caneta'
indice = 0
while indice < len(str):
    print(str[indice])
    indice = indice + 1

# Acessando elementos (Terceira maneira)
str = 'caneta'
for indice in range(0, len(str), 1):
    print(str[indice])

# Acessando elementos (Quarta maneira)
str = 'caneta'
for item in str:
    print(item)

