# Um inteiro positivo é chamado de número de Armstrong de ordem n se ..
# .Crie um programa usando for para encontrar todos os números de Armstrong dado um intervalo.
# Ex: 153 = 1 * 1 * 1 + 5 * 5 * 5 + 3 * 3 * 3

for a in range(12, 154):
    copia = a
    tamanho = len(str(a))
    armstrong = 0
    while a > 0:
        dig = a % 10
        armstrong += dig ** tamanho
        a = a // 10
    if armstrong == copia:
        print(f"O número {copia} é um número de armstrong")
    else:
        print(f"O número {copia} não é um número de armstrong")