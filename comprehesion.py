#list
M = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
print(list(map(sum,M)))
#comprehension syntax
set_compre = {sum(row) for row in M}
print(set_compre)
#set comprehension
set = {x**2 for x in [1, 2, 3, 4]}
print(set)
