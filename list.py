#create list
my_list = [1, 2, 3, 4, 5]
#accessing elements
first_item = my_list[0]
last_item = my_list[-1]
print(first_item, last_item)
#adding elements
my_list.append(6)
my_list.insert(0, 0)
print(my_list)
#removing elements
my_list.remove(3) #remove element as 3
#pop elements
popped_item = my_list.pop()
print(my_list)
print(popped_item)
#slicing
slicing_list = my_list[2: 5]
print(slicing_list)
#list lenght
length_list = len(my_list)
print(length_list)
#iterating through a list
for item in my_list:
	print(item)
#list Comprehension
squared = [x**2 for x in my_list]
print(squared)
#checking for existence
exists = 3 in my_list
print(exists)
#sorting a lip
sort_list = sorted(my_list)
reverse_list = list(reversed(my_list))
print(sort_list)
print(reverse_list)
