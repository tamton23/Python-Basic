#create sets
my_set = {1, 2, 3, 4, 5}
#adding elements
my_set.add(6)
print(my_set)
#checking existence
exists = 2 in my_set
#converting a list to a set
my_list = list(my_set)
my_list.append(2)
print(my_list)
unique_set = set(my_list)
print(unique_set)
#set operations
set_a = {1, 2, 3}
set_b = {3, 4, 5}

union = set_a | set_b
print(union)

intersection = set_a & set_b
print(intersection)

difference = set_a - set_b
print(difference)

symmetric_difference = set_a ^ set_b
print(symmetric_difference)

#removing elements raise error if not fond
#my_set.remove(7)
#removing does not raise error if not fond
my_set.discard(2)
print(my_set)
popped_item = my_set.pop()
print(popped_item)
print(my_set)
#cleaning set
my_sets = my_set.copy()
my_set.clear()
print(my_sets)
#iterating through a set
for item in my_sets:
	print(item)

#set comprehention
squared_set = {x**2 for x in my_sets}
print(squared_set)
#set_len

print(len(my_sets))
