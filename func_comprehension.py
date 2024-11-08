values = [2, 4, 9, 16, 25]

import math
res = []
for x in values: res.append(math.sqrt(x))

print(res)

print(list(map(lambda x: math.sqrt(x), values)))

print(list(map(math.sqrt, values)))

print([math.sqrt(x) for x in values])
