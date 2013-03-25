def merge_sort(vetor):
	left = []
  right = []
  result = []
  if (len(vetor)<=1):
		return vetor
  else:
    mid = (len(vetor))/2
    for x in range(mid):
	    left.append(vetor[x])
    for x in range(mid,len(vetor)):
			right.append(vetor[x])
    left = merge_sort(left)
    right = merge_sort(right)
    result = merge(left,right)
    return result
