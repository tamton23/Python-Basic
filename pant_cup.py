x = 4
while x > 0:
	print('\t' * (4 - x), '\tspam!' * x * 2)
	x -= 1

print('--------------------------*------------------------')

y = 10
str = 'spam!'
space = ' ' * len(str)
i = 0
while y > 0:
	print(space * i,str * y)
	i += 1
	y -= 2
	
