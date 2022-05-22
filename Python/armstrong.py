for i in range(10):

    n = int(input('\nenter a number: '))
    sum = 0
    temp = n
    while temp > 0:
        a = temp % 10
        sum += a**3
        temp //= 10
    if n == sum:
        print("it is an armstrong number")
    else:
        print("it is not an armstrong number")

    r = input('\nenter " y/n " to restart/exit: ')
    if r == "y":
        continue
    else:
        break
