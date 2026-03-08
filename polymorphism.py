class vehicle:
    def move(self):
        print ("all vehicles can move")

class car(vehicle):
    def move(self):
        print ("driving on road")

class bicyle(vehicle):
    def move(self):
        print ("pedaling on road")

v1 = vehicle()
c1 = car()
b1 = bicyle()

v1.move()
c1.move()
b1.move()