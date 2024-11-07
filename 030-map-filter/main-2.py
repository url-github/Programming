A = [1,2,3,4,5,6,7,8,9]

B = list(filter(lambda x: x % 2 == 0, A))
C = list(map(lambda x: x * 10, B))

print(C)