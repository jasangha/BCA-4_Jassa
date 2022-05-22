def func(x=None):
    result = " "
    if x is None:
        result = "No Arguments"
    elif x == 0:
        result = "Zero"
    elif 0 < x <= 3:
        result = "x is b\w 0 and 3"
    else:
        result = " x is more than 3"
    return result

print(func(-5))