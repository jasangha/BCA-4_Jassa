class stu:
    i = 1

    def __init__(self):
        global i
        i+1
        print(f'enter roll_no of {i} student: ', end=" ")
        rollno = int(input())
        print(f'enter name of {i} student: ', end=" ")
        name = str(input())

        self.rollno = rollno
        self.name = name

    def showdata(self):
        print(self.rollno, "\t", self.name)


list = []
n = int(input('enter number of students:'))

for i in range(n):
    list.append(stu())

print("\nRollno \tName\n------\t------")

for i in list:
    i.showdata()
