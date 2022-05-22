n=5

for row in range(0,n):
    for column in range(row+1,n):
        print(" ",end=" ")
    for column in range(0,row+1):#first triangle should be bigger to look pointy.
        print("*",end=" ")
    for column in range(0,row):
        print("*",end=" ")
    print()
# print("* * * * * * * * * * *")
for row in range(0,n):#inverted hill
    for column in range(0,row):
        print(" ",end=" ")
    for column in range(row+1,n):
        print("*",end=" ")
    for column in range(row,n):
        print("*",end=" ")
    print()