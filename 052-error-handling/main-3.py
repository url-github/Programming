line = input('Enter accepted price: ')
filepath =input('Enter filename : ')

file = open(filepath,'w+')
file.write(line)
file.close()