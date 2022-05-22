def fibonacci(n):
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, a+b
    return a


n = int(input('Enter a number: '))
print('Fibonacci seriers: ')
for i in range(n+1):
    print(i, ":", fibonacci(i))
