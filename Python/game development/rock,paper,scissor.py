for i in range(10):

    import random
    def pcturn(x):
        print('pc chose (',x,')')
   
    l=['r','p','s']
    a=input('choose(r,p,s): ')
    num=random.choice(l)

    if a=='r':
        pcturn(num)
        if num=='p':
            print('you lost !!!')
        elif num=='r':
            print('match draw !!!')
        else:
            print('you won !!!')
    elif a=='p':
        pcturn(num)
        if num=='s':
            print('you lost !!!')
        elif num=='p':
            print('match draw !!!')
        else:
            print('you won !!!')
    elif a=='s':
        pcturn(num)
        if num=='r':
            print('you lost !!!')
        elif num=='s':
            print('match draw !!!')
        else:
            print('you won !!!')
    else:
        print("values sahi bhar !!!")
    print()