for i in range(10):

    add=lambda x,y : x+y
    sub=lambda x,y : x-y
    mul=lambda x,y : x*y
    div=lambda x,y : x/y
    mod=lambda x,y : x%y

    a=int(input('\nenter first number: '))
    c=input('enter the operator(+,-,*,/,%): ')
    b=int(input('enter second number: '))
    if c=='+':
        print(a," + ",b," = ",add(a,b))
    elif c=='-':
        print(a," - ",b," = ",sub(a,b))
    elif c=='*':
        print(a," * ",b," = ",mul(a,b))
    elif c=='/':
        print(a," / ",b," = ",div(a,b))
    elif c=='%':
        print(a," % ",b," = ",mod(a,b))
    else:
        print('values sahi bhar oyeee!!!\n')

    a=input('\nenter "y/n" to restart/exit: ')
    if a=='y':
        continue
    else:
        print("program excited!!!!\n")
        break