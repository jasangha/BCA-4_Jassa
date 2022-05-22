mylist=[2,0,2,3,0,5,4,0,3,2,0,0,1,2,0,2]

def count_zeroes(lst):
    counter=0
    for i in lst:
        if i == 0:
            counter+=1
        return counter

def count_zeroes_recursively(lst):
    if len(lst) == 0:
        return 0
    if len(lst) == 1:
        return 1 if lst[0]==0 else 0
    if lst[0] == 0:
        return 1 + count_zeroes_recursively(lst[1:])
    else:
        return 0 + count_zeroes_recursively(lst[1:])

print(count_zeroes_recursively(mylist))
    