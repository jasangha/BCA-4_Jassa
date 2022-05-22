import colorama
import math


def progress_bar(progress, total, color=colorama.Fore.YELLOW):
    percent = 100 * (progress / float(total))
    bar = '#' * int(percent) + '-' * (100 - int(percent))
    print(color + f"\r|{bar}| {percent: .2f}%", end="\r")

    if progress == total:
        print(colorama.Fore.GREEN + f"\r|{bar}| {percent: .2f}%", end="\r")


def fib_recursive(n):
    if n == 1 or n == 2:
        return 1
    else:
        return(fib_recursive(n-1)+fib_recursive(n-2))


# numbers = [100]
# progress_bar(0, len(numbers))

# print('Fibonacci seriers: ')
# for i, x in enumerate(numbers):
#     progress_bar(i+1, len(numbers))
    # print(i, ":", fib_recursive(i))

numbers = [x * 5 for x in range(2000, 3000)]
results = []

progress_bar(0, len(numbers))
for i, x in enumerate(numbers):
    results.append(math.factorial(x))
    progress_bar(i+1, len(numbers))

print(colorama.Fore.RESET)
