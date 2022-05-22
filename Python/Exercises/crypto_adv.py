import random
import pickle


def encryptN(s):
    dict = {}
    string = ""

    for i in s:
        if i == '0':
            a = str(random.choice(
                [1, 2, 3, 5, 6, 7, 8, 9, '!', '@', '#', '$', '%', '&', '*', '_']))
            string += a
            dict[0] = a
            dict[0] = a
        elif i == '1':
            a = str(random.choice(
                [1, 2, 3, 4, 5, 6, 7, 8, 9, '!', '@', '#', '$', '%', '&', '*', '_']))
            string += a
            dict[1] = 0
            dict[1] = a
        elif i == '2':
            a = str(random.choice(
                [1, 2, 3, 4, 5, 6, 7, 8, 9, '!', '@', '#', '$', '%', '&', '*', '_']))
            string += a
            dict[2] = 0
            dict[2] = a
        elif i == '3':
            a = str(random.choice(
                [1, 2, 3, 4, 5, 6, 7, 8, 9, '!', '@', '#', '$', '%', '&', '*', '_']))
            string += a
            dict[3] = 0
            dict[3] = a
        elif i == '4':
            a = str(random.choice(
                [1, 2, 3, 4, 5, 6, 7, 8, 9, '!', '@', '#', '$', '%', '&', '*', '_']))
            string += a
            dict[4] = 0
            dict[4] = a
        elif i == '5':
            a = str(random.choice(
                [1, 2, 3, 4, 5, 6, 7, 8, 9, '!', '@', '#', '$', '%', '&', '*', '_']))
            string += a
            dict[5] = 0
            dict[5] = a
        elif i == '6':
            a = str(random.choice(
                [1, 2, 3, 4, 5, 6, 7, 8, 9, '!', '@', '#', '$', '%', '&', '*', '_']))
            string += a
            dict[6] = 0
            dict[6] = a
        elif i == '7':
            a = str(random.choice(
                [1, 2, 3, 4, 5, 6, 7, 8, 9, '!', '@', '#', '$', '%', '&', '*', '_']))
            string += a
            dict[7] = 0
            dict[7] = a
        elif i == '8':
            a = str(random.choice(
                [1, 2, 3, 4, 5, 6, 7, 8, 9, '!', '@', '#', '$', '%', '&', '*', '_']))
            string += a
            dict[8] = 0
            dict[8] = a
        elif i == '9':
            a = str(random.choice(
                [1, 2, 3, 4, 5, 6, 7, 8, 9, '!', '@', '#', '$', '%', '&', '*', '_']))
            string += a
            dict[9] = 0
            dict[9] = a
        else:
            string += '*'

    f = open('private_key.txt', 'wb')
    pickle.dump(dict, f)
    f.close()
    print("Encrypted Number:", string)


def decryptN(s):
    f = open('private_key.txt', 'rb')
    content = pickle.load(f)
    dict = content

    string = ""

    print(dict)
    for i in dict.keys():
        string += str(list(dict.keys())[i])
    # string.append(list(dict.keys())[i])
    print("Decrypted Number:", string)


option = input('enter (e) to encrypt, (d) to decrypt: ')
if option.lower() == 'e':
    code = input('enter number: ')
    a = tuple(code)
    encryptN(a)

else:
    # code = input('enter the encrypted code: ')
    # b = tuple(code)
    decryptN(0)
