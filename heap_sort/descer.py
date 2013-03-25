def descer(vetor, i, ultimo):
	j = 2*i
	if (j <= ultimo):
		if (j < ultimo):
			if (vetor[j] < vetor[j+1]):
				j += 1
			if (vetor[i] < vetor[j]):
				aux = vetor[i]
				vetor[i] = vetor[j]
				vetor[j] = aux
				descer(vetor, j, ultimo)
	return vetor
