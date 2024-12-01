def calculate(kind='+', *args):
	result = 0
	if kind == "+":
		for a in args:
			result +=a
	elif kind == "-":
		for a in args:
			result -=a
	return result

print(calculate('+',1,2,3))
print(calculate('-',1,2,3))
# 10
# 60

print("-"*30)

def create_functions(kind = "+"):
	source = '''
def f(*args):
	result = 0
	for a in args:
		result {}= a
	return result
'''.format(kind)
	exec(source, globals())

	return f

f_add = create_functions("+")
print(f_add(1,2,3,4))

f_subs = create_functions("-")
print(f_subs(10,20,30))
# 10
# -60