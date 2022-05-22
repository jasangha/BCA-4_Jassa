string = ""


def encryptA(s):
    global string
    for i in s:
        if i == "a":
            string += 'b'
        elif i == 'b':
            string += 'c'
        elif i == 'c':
            string += 'd'
        else:
            string += '.'
    print(string)


def encryptN(s):
    global string
    for i in s:
        if i == '0':
            string += str(9)
        elif i == '1':
            string += 'c'
        elif i == '2':
            string += 'a'
        elif i == '3':
            string += str(0)
        elif i == '4':
            string += 'x'
        elif i == '5':
            string += '#'
        elif i == '6':
            string += '&'
        elif i == '7':
            string += '@'
        elif i == '8':
            string += '!'
        elif i == '9':
            string += '$'
        else:
            string += '^'
    print(string)


def decryptN(s):
    global string
    for i in s:
        if i == '9':
            string += str(0)
        elif i == 'c':
            string += '1'
        elif i == 'a':
            string += '2'
        elif i == '0':
            string += str(3)
        elif i == 'x':
            string += '4'
        elif i == '#':
            string += '5'
        elif i == '&':
            string += '6'
        elif i == '@':
            string += '7'
        elif i == '!':
            string += '8'
        elif i == '$':
            string += '9'
        else:
            string += '^'
    print(string)


option = input('enter (e) to encrypt, (d) to decrypt: ')
if option == 'E' or option == 'e':
    encryptno = input('enter number: ')
    a = tuple(encryptno)
    encryptN(a)
else:
    decryptno = input('enter the encrypted code: ')
    b = tuple(decryptno)
    decryptN(b)
