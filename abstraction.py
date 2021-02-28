from abc import abstractmethod, ABC

class Vehicle(ABC):
    def __init__(self, brand,speed, year):
        self.speed = speed
        self.year = year
        self.brand=brand
    def __str__(self):
        return f'{self.brand}\n{self.speed}\n{self.year}'

    def start(self):
        print("Starting engine")

    def stop(self):
        print("Stopping engine")

    @abstractmethod
    def drive(self):
        print('driving the car..')

#create a class to inherit from
class Car(Vehicle):
    def __init__(self,brand, speed, year,mileage):
        super().__init__(brand,speed, year)
        self.mileage = mileage

    def drive(self):
        print("the Car is in drive mode")
    def start(self):
        print('The Car is starting')


car=Car('BMW','200km/h','2015',80000)
print(car)
car.drive()
car.start()
