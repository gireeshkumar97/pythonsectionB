class Parent:
    a=10
    b=210

    def __init__(self,c,d):
        self.c=c
        self.d=d
    def display(self):
        print(self.c,self.d)

class child(Parent):
    a=78

    def __init__(self,c,d,e,f):
        super().__init__(c,d)
        self.e=e
        self.f=f
    def display(self):
        Parent.display(self)
        print(self.e,self.f)

obj = child(5,8,3,5)