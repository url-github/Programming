firstRow = 1
lastRow = 5

currentRow = firstRow

while currentRow <= lastRow:
    print("Row number",currentRow)
    currentRow+=1

print("#################")

start = 1
end = 5

number = start

while number<=end:
    print(number, number*number, number*number*number)
    number+=1

print("#################")

start = 0
end = 5

x = start
while x<=end:
    print(x, 2**x)
    x+=1

print("#################")

start = 1
end   = 10
number = start

while number<=end:
    print(number*'x')
    number+=1