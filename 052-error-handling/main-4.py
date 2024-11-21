line = input('Enter accepted price: ')
filepath = input('Enter filename : ')

try:
    file = open(filepath,'w+')
    file.write(line)
    file.close()
except:
    print('SORRY WE HAVE AN ERROR. PLEASE TRY AGAIN')