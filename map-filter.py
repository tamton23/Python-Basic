#map(function, iterable1, iterable2, ...)
def muli(x):
	return x * x

result = map(muli, range(1, 5))
print(list(result))

#filter(function, iterable)

result = filter(lambda x:x % 2, range(1, 10))
print(list(result))


