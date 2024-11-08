def adder1(*args):
	print('adder1', end = ' ')
	#type  == 'int' init = 0
	if type(args[0]) == type(0):
		sum = 0
	else:
		sum = args[0][:0]
	for arg in args:
		sum = sum + arg
	return sum

def adder2(*args):
	print('adder2', end = ' ')
	#init = index 0
	sum = args[0]
	for next in args[1:]:
		sum += next
	return sum

for func in (adder1, adder2):
	print(func(2, 3, 4))
	print(func('spam', 'eggs', 'toast'))
	print(func(['a', 'b'], ['c', 'd'], ['e', 'f']))

