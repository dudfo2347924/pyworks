
class Car :
    def drive(self):
        print("차가 주행합니다.")

class Texi(Car) :
    def drive(self):
        print("택시가 주행합니다.")

class Bus(Car) :
    def drive(self):
        print("버스가 주행합니다.")

c = Car()
c.drive()

texi = Texi()
texi.drive()

bus = Bus()
bus.drive()