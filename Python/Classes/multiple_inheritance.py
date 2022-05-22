a,b=0,0
class father:
    def seta(x):
       global a
       a = x
class mother:
    def setb(x):
        global b
        b = x
class child(father,mother):
    def getc():
        print("child is a combination of mother(",a,") and father(",b,"):",a + b)

c=child
# f=father
# m=mother
# f.seta(5)
# m.setb(15)
c.seta(5)
c.setb(15)
c.getc()
  
