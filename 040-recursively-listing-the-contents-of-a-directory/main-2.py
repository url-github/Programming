import os

print('-'*30)
print(os.listdir(r"/Users/p/Documents/Scripts/Programming/040-recursively-listing-the-contents-of-a-directory/testowy"))
# ['b.txt', 'a.txt', 'zagniezdzony']

print('-'*30)
print(os.path.join(r"/Users/p/Documents/Scripts/Programming/040-recursively-listing-the-contents-of-a-directory/testowy", 'a.txt'))
# /Users/p/Documents/Scripts/Programming/040-recursively-listing-the-contents-of-a-directory/testowy/a.txt

print('-'*30)
print(os.path.isdir("/Users/p/Documents/Scripts/Programming/040-recursively-listing-the-contents-of-a-directory/testowy"))
# True