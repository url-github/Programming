import random

number_a = random.random() * 10
print(number_a)

number_float = random.uniform(0, 2)
print(number_float)


l = random.randint(a=1, b=2)
if l == 1:
	print(f'Wylosowano {l} -> orzeł')
else:
	print(f'Wylosowano {l} -> reszka')

