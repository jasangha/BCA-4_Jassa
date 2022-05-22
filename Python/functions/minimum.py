mylist = [10,99,12,5,4,12,8,3,9,100,1,55,43,22,3]

def find_min(lst):
    minimum = lst[0]
    for i in lst:
        if i < minimum:
            minimum = i
    return minimum

print(find_min(mylist))
