class Parent:
    a=10
    b=210

    def __init__(self,c,d): 
        self.c=c
        self.d=d

class child(Parent):
    a=78

    def __init__(self,c,d,e,f):
        super().__init__(c,d)
        self.e=e
        self.f=f
obj=child(4,5,6,7)
