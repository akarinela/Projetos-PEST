 # Crie uma função chamada intervalo que receba uma string e dois índices (int) como parâmetros de entrada e retorne a substring que está entre esses dois índices, incluindo o caractere no 
 # primeiro índice, mas excluindo o caractere no último índice. Ex: 'intervalo(”Python”, 1, 4)' deve retornar a substring “yth”

def intervalo(string: str, indices1: int, indices2: int):
    return string [indices1 : indices2]

print(intervalo('Python', 1, 4))