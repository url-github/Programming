import os

def CountWords(path):
    with open(path,'r', encoding='utf-8') as file:
        content = file.read()
        word_count = len(content.split())
    return word_count


path = path = r"/Users/p/Documents/Scripts/Programming/056-if-like-statement/main-3-file-1.txt"

if os.path.isfile(path):
    print("There are {} words in the file {}".format(CountWords(path), path))


os.path.isfile(path) and print("There are {} words in the file {}".format(CountWords(path), path))