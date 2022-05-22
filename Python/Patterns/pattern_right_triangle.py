n = 5  # int(input("enter a number: "))

for row in range(0, n):
    for column in range(0, row+1):
        print("*", end="   ")
    print()

# for row in range(0,n):#inverted right triangle
#     for column in range(row,n):
#         print("*",end="   ")
#     print()
