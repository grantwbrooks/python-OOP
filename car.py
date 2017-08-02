class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.milieage = mileage
        self.tax = .12
        if self.price > 10000:
            self.tax = .15
        else:
            self.tax = .12
        self.display_all()

    def display_all(self):
        print "Price:", self.price
        print "Speed:", self.speed, "mph"
        print "Fuel:", self.fuel
        print "Mileage:", self.milieage, "mpg"
        print "Tax:", self.tax
        return self

car1 = Car(2000,35,"Full",15)
car2 = Car(11000,49,"Empty",25)
car3 = Car(9000,50,"Half",45)
car4 = Car(1231,60,"Full",15)
car5 = Car(15000,205,"Half",10)
car6 = Car(10000,32,"Empty",25)

