def fact(n):
    if n < 0:
        print('Factorial does not exist for negative numbers!!!')
        return None
    elif n == 0 or n == 1:
        return 1
    else:
        return (n*fact(n-1))


a = int(input('enter a number: '))
print('Factorial of', a, 'is:', fact(a))
