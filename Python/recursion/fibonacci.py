def fib_recursive(n):
    if n == 1 or n == 2:
        return 1
    else:
        return(fib_recursive(n-1)+fib_recursive(n-2))


print('Fibonacci seriers: ')
for i in range(1, 10):
    print(i, ":", fib_recursive(i))
