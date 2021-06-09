from millerRabin import miller_rabin
from euclides import euclides, euclides_estendido
from codigo import códigos_para_símbolos, símbolos_para_códigos
from random import randrange

# Questão 9a.
def gera_primos(n):
    """
    Gera um número p primo de n algarismos
    Entrada: O tamanho do número p a ser gerado
    Saída: Um número primo que compreende o tamanho (10 ** n) < p < (10 ** n+2)
    """
    while True:
        primo = randrange(pow(10, n-1), pow(10, n+2))
        for _ in range(1, 11):
            base = randrange(1, primo)
            if miller_rabin(primo, base) == 'Composto':
                break
        else:
            break

    return primo

# Questão 9b.
def gera_chaves(a, b):
    """
    Gerador de chaves RSA 
    Entrada: 
    a -> Quantidade de algarismos de p para sorteio de um número primo p
    b -> Quantidade de algarismos de q para sorteio de um número primo q
    Saída: n, e, d, inverso de p mod q, inverso de q mod p, 
    forma reduzida de d mod p e d mod q
    """
    p, q = gera_primos(a), gera_primos(b)
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 2

    while euclides(e, phi) != 1:
        e += 1

    d = euclides_estendido(e, phi)
    inverso_de_p = euclides_estendido(p, q)
    inverso_de_q = euclides_estendido(q, p)
    dp_reduzido, dq_reduzido = pow(d, 1, p-1), pow(d, 1, q-1)

    if d < 0:
        d %= phi

    if inverso_de_p < 0:
        inverso_de_p %= q

    if inverso_de_q < 0:
        inverso_de_q %= p

    return n, e, d, p, q, inverso_de_p, inverso_de_q, dp_reduzido, dq_reduzido

# Questão 9c.
def gera_blocos(texto):
    """
    Quebra a mensagem em uma lista contendo um bloco de três em três
    Entrada: O texto a ser quebrado em blocos encriptados
    Saída: Bloco de mensagens encriptadas contendo os números 
    separados de três em três
    """
    blocos = list()
    for i in range(0, len(texto), 3):
        blocos.append(texto[i:i+3])
    return blocos

def encriptar(texto, n, e):
    """
    Encripta uma mensagem utilizando os conceitos de RSA
    Entrada: Texto a ser encriptado, expoente público, módulo público
    Saída: Bloco das mensagens encriptadas
    """
    for simb, cod in símbolos_para_códigos.items():
        texto = texto.replace(simb, str(cod))
    
    bloco_encriptado = gera_blocos(texto)
    for i in range(len(bloco_encriptado)):
        bloco_encriptado[i] = pow(int(bloco_encriptado[i]), e, n)
    
    return bloco_encriptado

# Questão 9d.
def descriptar(texto, n, d):
    """
    Descripta uma mensagem utilizando os conceitos de RSA
    Entrada: Texto encriptado, módulo público e expoente privado
    Saída: Mensagem descriptada
    """
    for i in range(len(texto)):
        texto[i] = pow(int(texto[i]), d, n)
        texto[i] = str(texto[i])
        for cod, simb in códigos_para_símbolos.items():
            if texto[i] == str(cod):
                texto[i] = simb

    mensagem = ''.join(texto)
    return mensagem

def descriptar_tcr(texto, n, d_mod_p, d_mod_q, p, q, inverso_p, inverso_q):
    """
    Descripta uma mensagem utilizando os conceitos de RSA
    com auxílio do Teorema Chinês do Resto para reduzir o sistema de congruência
    Entrada: Texto encriptado, módulo público, expoente privado mod p e mod q,
    o número primo p, o número primo q, o inverso de p mod q e
    o inverso de q mod p
    Saída: Mensagem descriptada 
    """
    for i in range(len(texto)):
        texto[i] = (pow(int(texto[i]), d_mod_q, q) * inverso_p * p) + (pow(int(texto[i]), d_mod_p, p) * q * inverso_q) 
        texto[i] = pow(texto[i], 1, n)
        texto[i] = str(texto[i])
        for cod, simb in códigos_para_símbolos.items():
            if texto[i] == str(cod):
                texto[i] = simb
 
    mensagem = ''.join(texto)
    return mensagem

print(gera_chaves(5, 7))
# Testes feitos a partir da chave gerada acima
print(descriptar(encriptar('Cebola da Indução', 6098822275103249, 7), 6098822275103249, 2613780564601783))
print(descriptar_tcr(encriptar('Cebola da Indução', 6098822275103249, 7), 6098822275103249, 2747623, 815389687, 6411121, 951287969, 830850597, 811677))