a=input('\na: ')
b=input('b: ')
try:
    print('a+b: ',int(a)+int(b))
except Exception as e:
    print('error:',e)
    print()
print('\nImportant line, printed even after an error.\n')
    