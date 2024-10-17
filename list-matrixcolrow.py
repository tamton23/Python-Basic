M = [[1, 2, 3],
     [4, 2, 3],
     [5, 2, 3]]
print(M)
# Collect the items in column 2
col1 = [row[0] for row in M]
print(col1)
# Add 1 to each item in column 2
col3 = [row[1] + 1 for row in M]
print(col3)
# Filter out odd items
col = [row[0] for row in M if row[1] % 2 == 0]
print(col)
# Collect a diagonal from matrix
diag = [M[i][i] for i in [0, 1, 2]]
print(diag)
# repeat character in a string
doubles = [c*2 for c in 'spam']
print(doubles)
# Create a generator of row sums
G = (sum(row) for row in M)
print(next(G))
# Run the iteration protocol
print(next(G))
# Map sum over items in M
print(list(map(sum, M)))
# Create a set of row sums
print({sum(row) for row in M}) #sets
# Creates key/value table of row sums
print({i : sum(M[i]) for i in range(3)}) #dictionaries

# List of character ordinals ASCII
print([ord(x) for x in 'Spaam'])
# Sets remove duplicates ASCII
print({ord(x) for x in 'Spaam'})
# Dictionary keys are unique ASCII
print({x:ord(x) for x in 'Spaam'})

