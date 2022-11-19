class SpaceObject():
    def __init__(self, raz, let):
        self.raz=raz
        self.let=let
class Star(SpaceObject):
    def __init__(self, yar):
        self.yar=yar
    def Svet(self):
        print(self.yar)
class Planet(SpaceObject):
    def __init__(self, nas, god):
        self.nas=nas
        self.god=god
    def Nas(self):
        print(self.nas)


