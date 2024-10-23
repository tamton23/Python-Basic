my_dict = {'name': 'alice', 'age': 25}

#accessing values
name = my_dict['name']
print(name)
age = my_dict['age']
print(age)
#adding/Updating Items
my_dict['city'] = 'An Giang'
my_dict['age'] = 26
print(my_dict)
#removing items
del my_dict['age']
value = my_dict.pop('city')
print(value)
print(my_dict)
#Iterating Through a Dictionary
my_dict['city'] = 'ho chi minh'
my_dict['age'] = 21
user = list(my_dict.keys())
for x in user:
	print(x, ' : ', my_dict[x]) 
#or
for key, value in my_dict.items():
	print(f'{key} : {value}')

#dictionary Comprehension
square_list = {x:x**2 for x in range(5)}
for key, value in square_list.items():
	print(f'{key} : {value}') #f have mean is format

#merging Dictionary 
another_dict = {'job': 'dev'}
merging_dict = {**my_dict,**another_dict}
print(merging_dict)
#checking for existence
exists = 'name' in my_dict
print(exists)
#dictionary length
lenght_dict = len(my_dict)
print(lenght_dict)
#Copying a dictionary
copy_dict = my_dict.copy()
print(copy_dict)
