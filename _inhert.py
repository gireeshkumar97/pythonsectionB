class Parent:
    a=10
    b=210

    def __init__(self,c,d):
        self.c=c
        self.d=d

class child(Parent):
    pass

obj = child(2,4)