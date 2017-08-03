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

product1 = Product(100,"Coolitem",29,"Nike",50).add_tax(.05).returned("opened box").display_info()
product2 = Product(200,"Cool item 2",19,"Adidas",30).display_info()


class Store(object):
    def __init__(self,location,owner):
        self.products = []
        self.location = location
        self.owner = owner
    
    def add_product(self,addedproduct):
        self.products.append(addedproduct)
        print self.products
        return self

    def remove_product(self,removedproduct):
        for prod in self.products:
            if prod.item_name == removedproduct:
                self.products.remove(prod)
        print self.products
        return self
    
    def inventory(self):
        for prod in self.products:
            print "Price:", prod.price
            print "Item Name:", prod.item_name
            print "Weight:", prod.weight
            print "Brand:", prod.brand
            print "Cost:", prod.cost
            print "Status:", prod.status
            print ""
        return self

store1 = Store("Miami","Grant").add_product(product1)
store1.add_product(product2)
store1.remove_product("Coolitem")
store1.inventory()










