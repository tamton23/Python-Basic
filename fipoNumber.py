def fipo(so):
	if so <= 1:
		return so
	return fipo(so - 1) + fipo(so -2)

for num in range(10):
	print(fipo(num))
