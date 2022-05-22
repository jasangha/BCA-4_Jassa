with open('jassa.txt', 'a') as file:
    file.write('Jassa\n')

with open('jassa.txt', 'r+') as file:
    content = file.read()
    print(content)
