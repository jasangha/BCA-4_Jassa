import random
l=[0,1,2,3,4,5,6,7,8,9]
a=random.choice(l)
for i in l:
    if i == 0 or i == 1 or i == 3:
        print(i,end=" ")

print(a)
    
print()
