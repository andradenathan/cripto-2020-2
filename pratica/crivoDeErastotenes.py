def crivo_erastotenes(n):
    """
    Crivo de erastótenes é um gerador de números primos até um certo limite n
    :param n: Limitador natural n >= 2
    :return: Lista de todos os números primos <= n
    """
    lista = [True] * n
    lista_primos = []

    lista[0] = False # 0 não é primo
    lista[1] = False # 1 não é primo

    for i in range(2, n):
        if lista[i]:
            for j in range(i ** 2, n, i):
                lista[j] = False

    for k in range(2, n):
        if lista[k]:
            lista_primos.append(k)

    return lista_primos