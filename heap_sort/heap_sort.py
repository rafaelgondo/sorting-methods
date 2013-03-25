def heap_sort(vetor):
	vetor = construir(vetor, len(vetor)-1)
	for i in range(len(vetor)-1,0,-1):
		aux = vetor[0]
		vetor[0] = vetor[i]
		vetor[i] = aux
		vetor = descer(vetor, 0, i-1)
	print vetor
