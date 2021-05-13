def numeros_altamente_compostos(n):
	dicionario = {}
	maior = 0
	
	# Passo 1 -> gerar um dicionário de divisores de 1 até n (incluindo o n)

	for x in range(1, n+1):
		divisores = 0
		for y in range(1, x+1):
			if x % y == 0:
				divisores += 1
		dicionario[x] = divisores

	# Passo 2 -> dado dicionário de divisores, descobrir quais são os números
	# altamente compostos respeitando a regra d(x) < d(y) e caso não seja 
	# eliminaremos os números não altamente compostos 
	
	for i in range(1, n+1):
		if maior >= dicionario.get(i):
			del dicionario[i]
		else:
			maior = dicionario.get(i)
	
	for k in dicionario.keys():
		print(k)

numeros_altamente_compostos(5000)