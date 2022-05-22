a=0
b=0
c=0
result=0
class simple_interest:
    def __init__(self,x,y,z):
        self.a=x
        self.b=y
        self.c=z
        self.result=x+self.a*float(self.b)*self.c/100
    def showdata(self):
        print('the amount',self.a,'after',self.b,end="")
        print('% simple interest for',self.c,'years:',self.result)

class compound_interest:
    def __init__(self,x,y,z):
        self.a=x
        self.b=y
        self.c=z
        self.result=self.a*pow((1+float(self.b)/100),self.c) 
    
    def showdata(self):
        print('the amount',self.a,'after',self.b,end="")
        print('% compound interest for',self.c,'years:',self.result)

a=simple_interest(100,10,10)
a.showdata()
b=compound_interest(100,10,10)
b.showdata()

