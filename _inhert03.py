class Parent1:
    a=10
    b=210

    def __init__(self,c,d):
        self.c=c
        self.d=d
    def display(self):
        print(self.c,self.d)

class parent2(Parent1):
    a=78

    def __init__(self,c,d,e,f):
        super().__init__(c,d)
        self.e=e
        self.f=f
    def display(self):
        parent2.display(self)
        print(self.e,self.f)
class child(parent2):
    a=40
    def __init__(self,c,d,e,f,g,h):
        super().__init__(c,d,e,f)
        self.g=g
        self.h=h
obj=child(4,5,6,7,8,9)
