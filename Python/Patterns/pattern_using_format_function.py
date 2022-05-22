n=5 #int(input('enter a number: '))

for row in range(0,n-1):
    for column in range(row,n-1):
        print("  ",end="  ")
    for column in range(0,row):
        print("{0}{0}".format(row,column),end="  ")
    for column in range(0,row+1):
        print("{0}{0}".format(row,column),end="  ")
    print()

for row in range(0,n):
    for column in range(0,row):
        print("  ",end="  ")
    for column in range(row,n-1):
        print("{0}{0}".format(row,column),end="  ")
    for column in range(row,n):
        print("{0}{0}".format(row,column),end="  ")
    print()
