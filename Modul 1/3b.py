def konsonan(x):
	isiK = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "t", "p", "q", "r", "s", "v", "w", "x", "y", "z", "B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "T", "P", "Q", "R", "S", "T", "W", "X", "Y", "Z", " "]
	hitung = 0
	jml = len(x)
	for i in x:
		if i in isiK:
			hitung += 1
	print("(",jml,",", hitung,")")
konsonan("Surakartaaaaa adalah")
