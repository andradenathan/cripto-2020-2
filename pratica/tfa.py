# Teorema Fundamental da Aritmética

def menor_fator(n):
    for divisor in range(2, n+1):
        if divisor ** 2 > n:
            return n

        if n % divisor == 0:
            return divisor

def fatoracao_em_primos(n):
    "Lista de primos cujo produto é n, tal que n natural e n >= 2"
    fatorar = n
    lista = []
    while fatorar > 2:
        p = menor_fator(fatorar)
        fatorar //= p # divisão inteira
        lista.append(p)
    return lista

print(fatoracao_em_primos(15))