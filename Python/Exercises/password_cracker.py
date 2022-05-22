import random
import colorama
from colorama import Fore, Back, Style

password = input(("Enter your password: "))

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
             'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
             'w', 'x', 'y', 'z', ]

guess = ""

while (guess != password):
    guess = ""

    for letter in range(len(password)):
        guess_letter = random.choice(numbers)
        guess += str(guess_letter)

    print(guess, end=" ")

colorama.init(autoreset=True)
print(f"{Fore.CYAN}{Style.BRIGHT}\n\t\t\t\t\t\tYour password is: ", end="")
print(f"{Fore.RED}{Style.BRIGHT}"+guess)
