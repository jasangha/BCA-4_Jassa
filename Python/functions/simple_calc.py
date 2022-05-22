def add(x,y) :
    print(x," + ",y," = ",x+y)
def sub(x,y) :
    return x-y
def mul(x,y) :
    return x*y

a=int(input('\nenter first number: '))
c=input('enter the operator(+,-,*): ')
b=int(input('enter second number: '))
if c=='+':
    add(a,b)
elif c=='-':
    print(a," - ",b," = ",sub(a,b))
elif c=='*':
    print(a," * ",b," = ",mul(a,b))
else:
    print('values sah bhar!!!!')
