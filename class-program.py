class phone :
    def make_call(self):
        print("making call")

    def play_game(self):
        print("playing game ")

    def set_colour(self,colour):
        self.colour=colour

    def show(self):
        return self.colour





p1=phone()

p2=phone()

p2.play_game()

p1.make_call()

p1.set_colour('red')

print(p1.show())



