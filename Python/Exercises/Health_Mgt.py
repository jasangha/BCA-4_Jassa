import datetime


def getdate():
    # import datetime
    return datetime.datetime.now()


def gettime():
    return datetime.datetime.now()


def take(k):
    if k == 1:
        c = int(input("enter 1 for excersise and 2 for food"))
        if(c == 1):
            value = input("type here\n")
            with open("jassa-ex.txt", "a") as op:
                op.write(str(gettime())+":"+value + "\n")
            print("successfully written")
        elif(c == 2):
            value = input("type here\n")
            with open("jassa-food.txt", "a") as op:
                op.write(str(gettime())+":"+value + "\n")
            print("successfully written")
    elif(k == 2):
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            value = input("type here\n")
            with open("rana-ex.txt", "a") as op:
                op.write(str(gettime())+":"+value + "\n")
            print("successfully written")
        elif (c == 2):
            value = input("type here\n")
            with open("rana-food.txt", "a") as op:
                op.write(str(gettime())+":"+value + "\n")
            print("successfully written")
    elif(k == 3):
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            value = input("type here\n")
            with open("musu-ex.txt", "a") as op:
                op.write(str(gettime())+":"+value + "\n")
            print("successfully written")
        elif (c == 2):
            value = input("type here\n")
            with open("musu-food.txt", "a") as op:
                op.write(str(gettime())+":"+value + "\n")
            print("successfully written")
    else:
        print("plz enter valid input (1(jassa),2(rana),3(musu)")


def retrieve(k):
    if k == 1:
        c = int(input("enter 1 for excersise and 2 for food"))
        if(c == 1):
            with open("jassa-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif(c == 2):
            with open("jassa-food.txt") as op:
                for i in op:
                    print(i, end="")
    elif(k == 2):
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            with open("Rana-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif (c == 2):
            with open("Rana-food.txt") as op:
                for i in op:
                    print(i, end="")
    elif(k == 3):
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            with open("Mussu-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif (c == 2):
            with open("Mussu-food.txt") as op:
                for i in op:
                    print(i, end="")
    else:
        print("plz enter valid input (harry,rohan,hammad)")


print("health management system: ")
a = int(input("Press 1 for log the value and 2 for retrieve "))

if a == 1:
    b = int(input("Press 1 for Jassa 2 for Rana 3 for Mussu "))
    take(b)
else:
    b = int(input("Press 1 for  2 for Rana 3 for Mussu "))
    retrieve(b)
