l = [lambda x, y: x+y,
     lambda x, y: x-y,
     lambda x, y: x*y,
     lambda x, y: x/y,
     lambda x, y: x % y]


def setop(c):
    if c == '+':
        return 0
    elif c == '-':
        return 1
    elif c == '*':
        return 2
    elif c == '/':
        return 3
    elif c == '%':
        return 4
    else:
        print("values sahi bhar")


a = int(input('\nenter first number: '))
b = int(input('enter second number: '))
c = input('enter the operator(+,-,*,/,%):')

index = setop(c)

print('result: ', l[index](a, b))
