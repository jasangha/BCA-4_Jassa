n=5#int(input("enter a number: "))
ch=65
for row in range(0,n):
    for column in range(0,row+1):
        print((chr(ch)),end="   ")
    print()

ch=64 
for row in range(0,n):
    for column in range(1,row+2):
        print((chr(ch+column)),end="   ")
    print()
    
for row in range(1,n+1):
    for column in range(0,row):
        print("{0}".format(chr(ch+row)),end="   ")
    print()
