var_x = 10
password = 'jhjchwcFRWfw434'
source = 'var_x + 5' # Fragment kodu od uytkownika
# source = 'password' # Fragment kodu od uytkownika

print("-"*20)
globals = globals().copy()
del globals['password']

result = eval(source, globals)
print(result) # 15

# print(globals())
# {'__name__': '__main__', '__doc__': None, '__package__': None,
# '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x102720ca0>,
# '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>,
# '__file__': '/Users/p/Documents/Scripts/Programming/064-eval/main-1.py',
# '__cached__': None,
# 'var_x': 10, 'password': 'jhjchwcFRWfw434',
# 'source1': 'var_x + 5', 'source2': 'password',
# 'result1': 15, 'result2': 'jhjchwcFRWfw434'}

print("-"*20)




