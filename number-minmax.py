a = [5, 7, 3, 9, 2, 4]
min = a[0]
for i in a:
	min = ((min+i)-abs(min-i))/2
print(min)
