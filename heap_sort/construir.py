def construir(vetor, ultimo):
	for i in range(ultimo/2, -1, -1):
		vetor = descer(vetor, i, ultimo)
	return vetor
