# Número Altamente Composto
# Definição: seja d(x) os divisores de um número x inteiro qualquer, tal que se d(x) < d(y)
# então d(x) é um número altamente composto.

def numeros_altamente_compostos(n):
    lista = [[]]
    lista_numeros_altamente_compostos = []
    for x in range(1, n + 1):
        divisores = 0
        for y in range(1, x + 1):
            if x % y == 0:
                divisores += 1
        lista.append(divisores)

    for i in range(1, n+1):
        contador = 0
        quant_divisores = lista[i]
        for j in range(1, i):
            if lista[j] >= quant_divisores:
                contador += 1
        if contador == 0:
            lista_numeros_altamente_compostos.append(i)

    return lista_numeros_altamente_compostos

print(numeros_altamente_compostos(5000))

