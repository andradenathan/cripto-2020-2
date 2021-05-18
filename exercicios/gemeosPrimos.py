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

def gemeos_primos(k, limite):
	"""
	k-gêmeos são definidos por números primos que distam k um do outro
	param k: int -> int
	param limite: int -> int
	return: list -> list
	"""
	lista_primos = crivo_erastotenes(limite)
	lista_kgemeos_primos = []
	for i in range(len(lista_primos)):
		if (lista_primos[i] + k) in lista_primos:
			lista_kgemeos_primos.append([lista_primos[i], lista_primos[i] + k])

	return lista_kgemeos_primos

print(gemeos_primos(10, 10000))
