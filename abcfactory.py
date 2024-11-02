from abc import ABC, abstractmethod

class Car(ABC):
    @abstractmethod
    def detail(self):
        pass

    def model(self):
        pass

class  DetailBase(ABC):
    @abstractmethod
    def show(self):
        pass

class BMWDetail(DetailBase):
    def __init__(self, car):
        self.car = car
    def show(self):
        return f'BMW detail:\t price {self.car.price}\t model {self.car.mod}\t color {self.car.color}'

class BenzDetail(DetailBase):
    def __init__(self, car):
        self.car = car
    def show(self):
        return f'Benz detail:\t price {self.car.price}\t model {self.car.mod}\t color {self.car.color}'

class BMW(Car):
    def __init__(self,mod, price,color):
        self.mod = mod
        self.price = price
        self.color = color

    @property
    def detail(self):
        return BMWDetail(self)

    @property
    def model(self):
        return

class Benz(Car):
    def __init__(self, mod, price,color):
        self.mod = mod
        self.price = price
        self.color = color

    @property
    def detail(self):
        return BenzDetail(self)

    @property
    def model(self):
        return

if __name__ == '__main__':
    bmw = BMW('coupe','12','white')
    benz = Benz('coupe','13','black')

    cars = [bmw,benz]
    for car in cars:
        print(car.detail.show())