def euclides(a, b):
    "Executa mdc(a, b) para a & b naturais > 0"
    if b == 0:
        return a
    else:
        return euclides(b, a % b)

def euclides_estendido(a, b):
    "Calcula o mdc(a, b), x & y tais que x, y sejam inteiros"
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

        print(dividendo, x_antigo, y_antigo)
    return dividendo, x_antigo, y_antigo