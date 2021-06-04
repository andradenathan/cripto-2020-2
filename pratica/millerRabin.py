def fatoracao(n):
    "Retorna k, q com q ímpar"
    k = 0
    q = n
    while q % 2 == 0:
        q //= 2
        k+= 1
    return k, q


def miller_rabin(mod, base):
    if mod % 2 == 0 or mod == 1:
        return 'Composto'
    base %= mod
    if base == 0 or base == 1:
        return 'Inconclusivo'

    if base == 1 or base == mod-1:
        return 'Inconclusivo'

    k, q = fatoracao(mod-1)
    r = pow(base, q, mod)
    i = 0
    while True:
        r = pow(r, 2, mod)
        i += 1

        if r == 1 or i == k:
            return 'Composto'
        if r == mod-1:
            return 'Inconclusivo'

print(miller_rabin(341, 2))