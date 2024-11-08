#create a tuple
my_tuple = (1, 2, 3, 4, 5)
#accessing elements
first_item = my_tuple[0]
last_item = my_tuple[-1]
print('firts:', first_item, 'last:', last_item)
#Single-Elements tuple
single_item = (1,) #include a comma
single = (1) #int or string
print(single_item)
print(single)
#iterating through a tuple
for item in my_tuple:
	print('tuple:', item)

#tuple are immutable: numbers, string, tuples
#my_tuple[0] = 1 => error

#length of tuple
print(len(my_tuple))
#repeating tuple
repeated_tuple = (1, 2) * 2
print('repeating:', repeated_tuple)
#packing and unpacking
packed = (1, 2, 3)

a, b, c = packed
print('a:', a, 'b:', b, 'c:', c)

#slicing
sub_tuple = my_tuple[:2]
print(sub_tuple)
#comcatenating tuple
new_tuple = my_tuple + (6, 7)
print(new_tuple)
