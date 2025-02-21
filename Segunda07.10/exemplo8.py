# str = 'uva'
# str[2] = '@'

# print(str) #ERRO
# não como alterar strings, só substituir 

str = 'Hoje é um bom dia'

inicio = str[0:10]
fim = str[13:]

novastr = inicio + 'mal' + fim
print(novastr)

# existe duas possíveis operações com strings:
# 1 - "somar" é concatenar strings

str = 'olá' + ' ' + 'mundo' + '10'
print(str)

# 2 - "multiplicar" é repetir strings
str = 'olá' * 4
print(str)