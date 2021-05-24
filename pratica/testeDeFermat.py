def fermat(base, modulo):
    """
    Retorna um teste inconclusivo ou composto de acordo com o Teste de Fermat
    """
    if pow(base, modulo, modulo) == (base % modulo):
        return 'Inconclusivo'
    return 'Composto'

print(fermat(2, 341))