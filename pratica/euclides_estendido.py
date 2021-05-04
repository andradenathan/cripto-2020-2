def euclides_estendido(a, b):
    """
    :param a: int -> int
    :param b: int -> int
    :return: mdc(a, b), x e y
    """
    x_antigo = 1
    y_antigo = 0

    x_novo = 0
    y_novo = 1

    dividendo = a
    divisor = b

    while divisor != 0:
        resto = dividendo % divisor
        quociente = dividendo // divisor

        x_antigo, x_novo = x_novo, (x_antigo - (x_novo * quociente))
        y_antigo, y_novo = y_novo, (y_antigo - (y_novo * quociente))

        dividendo, divisor = divisor, resto

    return dividendo, x_antigo, y_antigo

print(euclides_estendido(561, 1995))