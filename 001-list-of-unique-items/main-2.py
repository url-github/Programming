a = "abcdefg"
print(a[1])
# a[1] = "X" # stringi są niemutowalne, co oznacza, że nie można zmieniać ich zawartości bezpośrednio.

print("###")

a = list("abcdefg")
a[1] = "X"
result = "".join(a)
print(result)

print("###")

a = 'abcdefg'
print(id(a))
a_lista = list(a)
a_lista[1] = 'X'
a = ''.join(a_lista)
print(id(a))

print("###")

b = ['a', 'b', 'c', 'd', 'e']
print(id(b))
b[1] = "Y"
print(id(b))

print("###")

c = ['a', 'b', 'c', 'd', 'e']
print(id(c))
print(type(c))
c[1] = "Y"
result = ''.join(c)
print(id(result))
print(type(result))


# int, float, bool, str, tuple, frozenset - obiekty niezmienne
# list, set, dict - obiekty zmienne