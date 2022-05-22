for i in range(10):

    def sum(n):
        add=0
        while n>0:
            t=n%10
            add+=t
            n//=10
        return print('sum of digits: ',add)
    
    a=int(input('enter a number: '))
    sum(a)
    print()
    
    a=input('enter (y/n) to restart/exit: ')
    if a=='y':
        continue
    else:
        print('program excited!!!!')
        break
    print()