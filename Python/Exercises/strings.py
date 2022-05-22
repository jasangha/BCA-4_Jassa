s1 = ' ##Jassa Boss## '.rstrip().lstrip().strip(
    '#').strip('Boss').replace(' ', '^').split(" ", maxsplit=1)

s2 = "jassa".count('s')
s3 = "Jassa".find('s', 2)  # start from index 2, rfind(), lfind()

# s2 = ' ##_Jassa_Boss## '.removeprefix('#').removesuffix('#')
# rsplit, lsplit
# islower() isupper() istitle() isnumeric() .isalpha() .isalnum() ==> True or False

list_of_string = ['jassa', 'boss', 'jassa boss', 'jassa boss jassa boss']
s4 = ' * '.join(list_of_string)
print(s1, "\n", s2, "\n", s3, "\n", s4)

print("Jassa".startswith("J"))
print("Jassa".endswith("sa"))

s5 = "Jassa is Boss".swapcase().partition('IS')
print(s5)

s6 = "-52".zfill(5)
print(s6)

s7 = 'Jassa'
s7 = s7.rjust(12, '*')  # ljust
print(s7)

s8 = 'Jassa'
s8 = s8.center(20, "*")
print(s8)

num = "123456789"
string = "Jassa"
s9 = f'My name is {string} and my number is {num}'
print(s9)
