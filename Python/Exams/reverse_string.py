def rev(str):
    rev = ''
    index = len(str)-1
    while index >= 0:
        rev += str[index]
        index = index-1
    return rev

a=input('\nenter a string: ')
print('reverse : ',rev(a),"\n")
