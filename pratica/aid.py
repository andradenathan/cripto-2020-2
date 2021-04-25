# Algoritmo Ingênuo da Divisão

def aid(a, b):
    """
    Recebe naturais a, b com b != 0 e retorna naturais q, r com a = b * q + r tal que b > r.
    :param a: int
    :param b: int
    :return: int
    """
    Q = 0
    R = a
    while R >= b:
        R -= b
        Q += 1

    return Q, R

print(aid(80001, 5))
