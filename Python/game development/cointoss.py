import random
import os
import getch


def pause():
    print('choose (heads or tails) and press enter.')
    getch.getch()


l = ['Heads', 'Tails']
rand = random.choice(l)

print('choose (heads or tails) and press enter.')
a = input()
# a = input('').split(" ")[0]
pause()
print('Result:', rand)
file = "jassa.wav"
os.system(file)
