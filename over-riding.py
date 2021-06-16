class vehicle :

    def __init__(self,milege,cost):
        self.milege=milege
        self.cost=cost

    def show(self):
        print("milege",self.milege)
        print("cost",self.cost)


class car(vehicle):
    def __init__(self,milege,cost,tyre,hp):
        super().__init__(milege,cost)
        self.tyre=tyre
        self.hp=hp

    def show_car(self):
        print("i am a car")
        print("numbe of tyzre",self.tyre)
        print("HP",self.hp)
        print("milege",self.milege)


c1=car(600,99999999,4,800)
c1.show_car()
