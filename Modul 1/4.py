def rerata(x):
	k = len(x)
	j = 0
	for i in range (k):
		j += x[i]
		c = j/k
	print(c)
rerata([1, 2, 3, 4, 5])
