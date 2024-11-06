g = 'jestem globalna'

def f():
    global g
    g = 'teraz jestem lokalna'
    print(g)

f()
print(g)