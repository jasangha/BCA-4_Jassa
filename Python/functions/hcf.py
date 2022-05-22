def hcf(x,y):
    if x>y:
        smaller=y
    else:
        smaller=x
    for i in range(1,smaller+1):
        if(x%i==0)and(y%i==0):
            hcf=i
    return hcf
a=int(input('enter first number: '))
b=int(input('enter second number: '))
print('HCF of ',a,' and ',b,': ',hcf(a,b))