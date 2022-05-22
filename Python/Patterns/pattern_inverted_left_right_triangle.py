n=5

for row in range(0,n):
    for column in range(row,n):
        print(" ",end="   ")
    for column in range(0,row+1):
        print("*",end="   ")
    print()

for row in range(0,n):
    for column in range(0,row+1):
        print(" ",end="   ")
    for column in range(row,n):
        print("*",end="   ")
    print()