i = 10
result = 1

for j in range(1,i+1):
    result *= j

print(i, result)

print('------------')

import math
print(10, math.factorial(10))

print('------------')

x = 10
for i in range(1, x+1):
    result = 1

    for j in range(1, i+1):
        result *= j

    print(i, result)

print('------------')

list_noun = ['dog', 'potato', 'meal', 'icecream', 'car']
list_adj = ['dirty', 'big', 'hot', 'colorful', 'fast']

for noun in list_noun:
    for adj in list_adj:
        print(adj, noun)