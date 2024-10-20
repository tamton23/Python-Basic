rec = {'name': {'first': 'Tam', 'last': 'Ton'}, #dictionary
	'job': ['dev', 'student'], #list
	'hoppi': {'game', 'food'}, #sets
	'age': 21} #int

print(rec['name']['first'])
print(rec['job'][-1])

print(rec)
#add 1 job (only list)
rec['job'].append('mgr')
print(rec['job'])
#add 1 hoppi (only sets)
rec['hoppi'].add('music')
print(rec['hoppi'])
