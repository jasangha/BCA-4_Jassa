dict = {'a':10, 'b':20, 'c':30, 'd':40, 'e':50}
# for i in range(5):
#     a = 0
#     a += list(dict.values())[i]
#     print(a)
a = []
for i in dict:
    a.append(dict[i])
final = sum(a)
print(final)

# b = 0
# for i in a:
#     b += i

# print(b)
