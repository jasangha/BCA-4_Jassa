a, b, c = 50, 40, 60

if a < b and a < c:
    print("A")
elif b < a and b < c:
    print("B")
else:
    print("C")

def min(x, y, z):
    min = x
    for i in range(3):
        if i < min:
            min = i
    return min
print(min(a, b, c))
