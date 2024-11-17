import os
pwd = os.getcwd()

name = 'Python'
print(f'Cześć, {name}')

name = 'Python'
print('Cześć, {}'.format(name))

name = 'John'
age = 25
height = 180.5

print('My name is', name, 'and I\'m', age, 'years old.')
print('My height is', height, 'cm.')

print(f'My name is {name} and I\'m {age} years old.')
print(f'My height is {height} cm.')

name = 'Alice'
age = 30
height = 165.5
print(name, age, height, sep='|')