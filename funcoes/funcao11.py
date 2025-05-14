# Defina uma função chamada eh_primo que aceita um número como parâmetro e retorna True se o número for primo e False caso contrário.

def eh_primo(num):
    primo = 0
    for i in range(num):
        i += 1
        if num % i == 0:
            primo += 1
    if primo == 2:
        return True
    else:
        return False

num = int(input('Digite um número: '))

resul = eh_primo(num)

print(resul)