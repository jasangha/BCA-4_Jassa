class stu:
        def __init__(self):
                i=0
                rollno=int(input('enter roll_no of'''',i,''''student: '))
                name=input('enter name of'''',i,''''student: ')
                # course=input('enter your course: ')
                i+1
                self.rollno=rollno
                self.name=name
                
        def showdata(self):
                 print(self.rollno,"\t",self.name)

list=[]
n=int(input('enter number of students:'))
for i in range(n):
        list.append(stu())
print("\nRollno \tName\n------\t------")
for i in list:
        i.showdata()
