def mdc_ingenuo(a, b):
    divisor = numero_atual = 1
    while numero_atual < min(a, b):
        numero_atual += 1
        if a % numero_atual == 0 and b % numero_atual == 0:
            divisor = numero_atual

    return divisor


def algoritmo_euclidiano(a, b):
    if b == 0:
        return a

    else:
        return algoritmo_euclidiano(b, a % b)

print(algoritmo_euclidiano(27282828221113327892728282822111332789272828282211133278927282828221113327891133, 3223427282828221113328889978927282828221113327892728282822111332789644136612423976))
