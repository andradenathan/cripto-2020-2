def hanoi(n, origem, destino, auxiliar):
	"""
	param n: quantidade de discos
	param origem: pino origem
	param destino: pino destino
	param auxiliar: pino auxiliar
	O objetivo do jogo é fazer com que passe de um pino ao destino os n-1's
	objetos, com a ajuda do pino auxiliar.
	"""
	if n == 1:
		print(f"De {origem} para {destino}")

	else:
		hanoi(n-1, origem, auxiliar, destino)
		print(f"De {origem} para {destino}")
		hanoi(n-1, auxiliar, destino, origem)

hanoi(10, "origem", "destino", "auxiliar")