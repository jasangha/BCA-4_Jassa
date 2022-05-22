# f =open('jassa.txt','a')#'w' for write,replace previous data. "a" for append,append into previous data
f = open('jassa.txt', 'r+')  # read and write both
f.write("JASSA")

f = open('jassa.txt', 'r+')  # read and write both
b = f.read()
print(b)

f.close()
