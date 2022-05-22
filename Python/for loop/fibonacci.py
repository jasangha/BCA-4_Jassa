n=int(input('enter a number= '))
a=0
b=1
print('fibonacci series of',n,'is: ',end='')
for i in range(0,n-2):
    c=a+b
    print(c,end=',')
    a=b
    b=c