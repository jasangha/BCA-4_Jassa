def pal(x):
    l=0
    r=len(x)-1

    while r>=l:
        if not x[l]==x[r]:
            return('it is not palindrome')
        l+=1
        r-=1
    return('it is palindrome')

a=input('\nenter a string: ')
print(pal(a),'\n')