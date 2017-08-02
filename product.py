class Product(object):
    def __init__(self, price, item_name, weight, brand, cost):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = "for sale"

    def sell(self):
        self.status = "sold"
        return self

    def add_tax(self,tax):
        self.tax = tax
        self.price = (self.tax * self.price) + self.price
        return self
    
    def returned(self, reason):
        self.reason = reason
        if self.reason == "defective":
            self.status = "defective"
            self.price = 0
        if self.reason == "in the box":
            self.satus = "for sale"
        if self.reason == "opened box":
            self.status == "used"
            self.price = self.price*.80
        return self

    def display_info(self):
        print "Price:", self.price
        print "Item Name:", self.item_name
        print "Weight:", self.weight
        print "Brand:", self.brand
        print "Cost:", self.cost
        print "Status:", self.status
        return self

x1 = Product(100,"Cool item",29,"Nike",50).add_tax(.05).returned("opened box").display_info()
