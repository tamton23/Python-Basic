#!/usr/bin/python
# eq: ax + b = 0

a = input('a = ')
b = input('b = ')

if (a==0):
	if (b==0):
		print 'PT vo dinh'
	else:
		print 'PT vo nghiem'
else:
	x = -1.0*b/a
	print 'x = ',x
	