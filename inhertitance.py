class vehicle :

    def __init__(self,milege,cost):
        self.milege=milege
        self.cost=cost

    def show(self):
        print("milege",self.milege)
        print("cost",self.cost)


v1=vehicle(300,555555)

v1.show()


class car(vehicle):
       def show_car(self):
           print("i am a car")

c1=car(250,66666)

c1.show_car()
c1.show()