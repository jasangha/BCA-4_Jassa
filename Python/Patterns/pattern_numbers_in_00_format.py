n=5
sum=0
bum=0
for row in range(0,n):
    for column in range(0,row+1):
        sum+=1
        print("{:02d}".format(sum),end="   ")
    print()
for row in range(-1,n):
    for column in range(row,n):
        bum+=1
        print("{:02d}".format(bum),end="   ")
    print()

