n=5#int(input("enter a number: "))

for row in range(1,n+1):
    for column in range(1,row+1):
        print(column,end="   ")
    print()

print(">>>>>>>>>>>>>>>>>>>>")

for row in range(n,0,-1):#inverted
    for column in range(1,row+1):
        print(row,end="   ")
    print()
