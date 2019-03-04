def vokal(x):
	isiV = ["a", "i", "u", "e", "o", "A", "I", "U", "E", "O", " "]
	hitung = 0
	jml = len(x)

	for i in x:
		if i in isiV:
			hitung += 1
	print("(",jml,",", hitung,")")
vokal("Surakartaaaaa")

