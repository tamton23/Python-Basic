D = {'a': 1, 'c': 3, 'b': 2}
#add key e value = 99 in dictionaries
D['e'] = 99
print(D)
#if
if not 'f' in D:
	print('missing')
#replace if as if(true) = x; if(false) = 0
value = D.get('x', 0)
print(value)
#replace if(true)
value = D.get('a', 0)
print(value)
# if true
value = D['c'] if 'c' in D else 0
print(value)
