# 2 - Leia duas string do usuário e escreva na tela qual das duas é a maior string

str1 = input('Escreva uma string: ')
str2 = input('Escreva outra string: ')

tamanho1 = len(str1)
tamanho2 = len(str2)

if tamanho1 > tamanho2:
    print(f'{str1} é maior')
elif tamanho2 > tamanho1:
    print(f'{str2} é maior')
else:
    print(f'{str1} e {str2} são iguais')