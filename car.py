class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.milieage = mileage
        self.tax = .12
        if self.price > 10000:
            self.tax = .15
        self.display_all()
    def display_all(self):
        print "Price:", self.price
        print "Speed:", self.speed
        print "Fuel:", self.fuel
        print "Mileage:", self.milieage
        print "Tax:", self.tax
        return self

car1 = Car(2000,"35mph","Full","15mpg")
car2 = Car(11000,"30mph","Empty","25mpg")
car3 = Car(9000,"50mph","Half","45mpg")
car4 = Car(1231,"70mph","Full","15mpg")
car5 = Car(15000,"205mph","Half","10mpg")
car6 = Car(10000,"32mph","Empty","25mpg")

