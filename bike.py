class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    def displayInfo(self):
        print "Price:", self.price
        print "Max Speed:", self.max_speed
        print "Miles:", self.miles
        return self
    def ride(self):
        print "Riding..."
        self.miles += 10
        return self
    def reverse(self):
        print "Reversing..."
        self.miles -= 5
        #prevent neg miles
        if self.miles < 0:
            self.miles = 0
        return self
    


bike1 = Bike(200, "25mpg")
bike2 = Bike(250, "30mpg")
bike3 = Bike(300, "55mpg")

bike1.ride().ride().ride().reverse().displayInfo()
bike2.ride().ride().reverse().reverse().displayInfo()
bike3.reverse().reverse().reverse().displayInfo()

    