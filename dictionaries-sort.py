D = {'a': 1, 'b': 2, 'c': 3}
print(D)

#print keys
print(list(D.keys()))
#print values
print(list(D.values()))
# init ks = Keys
ks = list(D.keys())
#reverse list
ks.reverse()
for key in ks:
	print(key, '=>', D[key])

#reverse dictionaries

for key in reversed(D):
	print(key, '=>', D[key])

