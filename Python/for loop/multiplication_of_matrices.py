for i in range(10):
    x=[[2,3],[2,1],[5,3]]
    y=[[5,3,2],[2,1,4]]
    result=[[0,0,0],[0,0,0],[0,0,0]]
#we can only muiltiply two matrices, when the number of row of x is equals to the number of columns of Y.
    for i in range(len(x)):#number of rows of x
        for j in range(len(y[0])):#number of columns of y
            for k in range(len(y)):#number of rows of y
                result[i][j]+=x[i][k]*y[k][j]
#print(result)
    for i in result:
        print(i)

    a=int(input('enter " 0 " to restart: '))
    if a==0:
        continue
    else:
        break   
