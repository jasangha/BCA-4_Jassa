a = open("jassa.txt")
b = dict()

for line in a:
    line = line.strip()# removes \n,etc
    line = line.lower()# covert into lowercases
    words = line.split()# split lines into words

    for word in words:
        if word in b:
            b[word] = b[word]+1
        else:
            b[word] = 1

for i in list(b.keys()):
    print(i,":",b[i])
        



    
