def addDict(d1, d2):
	new ={}
	for key in d1.keys():
		new[key] = d1[key]
	for key in d2.keys():
		new[key] = d2[key]
	return new
