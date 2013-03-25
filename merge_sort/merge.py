def merge(left,right):
	result = []
  i = 0
  j = 0
  while (len(left)>0)and (len(right)>0):
	  if (left[0] <= right[0]):
	    result.append(left[0])
      left = left[1:]
    else:
      result.append(right[0])
      right = right[1:]
	if (len(left)>0):
	  result.extend(left)
  if (len(right)>0):
		result.extend(right)
  return result
