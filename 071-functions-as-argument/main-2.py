def say_hello(name):
    print("Hello {}!".format(name))

def say_good_morning(name):
    print("Good morning {}!".format(name))

def greet(how, name):
    how(name) # say_hello('Captain')

greet(say_hello, 'Captain')
# Hello Captain!

("-"*30)
