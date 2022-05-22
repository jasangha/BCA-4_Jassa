def fact(x):
    fact=1
    if x<0:
        print('enter a positive number')
    elif x==0:
        print('factorial of 0 is: 1')
    else:
        for i in range(x):
            fact = fact * (i+1)
        print('factorial of',x,'is:',fact)
    print()

for i in range(5):
    a=int(input('\nenter a number: '))
    fact(a) 