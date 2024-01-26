class Mtca:
    chairman = 'Mr.sunil'
    location = 'palamaner'
    collage = 'MTCA'

    def __init__(self,name,mobile):
        self.name= name
        self.mobile= mobile

class Mca(Mtca):
    principal = 'Mr.Mohamod Bilal'
    strength = 240
    staff =9
class Btech(Mtca):
    principal = 'Mis.Prashanthi'
    strength = 350
    staff = 35

Anvithaa = Mca('jassu',9398518088)
keshava = Btech('keshava',9578248121)