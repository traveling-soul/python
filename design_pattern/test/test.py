class Coffee:
    name = ""
    price = 0
    def __init__(self,name):
        self.name = name
        self.price = len(name)
    def show(self):
        print("Coffee Name:%s Price:%s"%(self.name,self.price))
class Customer:
    name = ""
    coffee_factory = ""
    def __init__(self,name,coffee_factory):
        self.name = name
        self.coffee_factory = coffee_factory
    def order(self,coffee_name):
        print("%s order a cup of coffee:%s" % (self.name, coffee_name))
        return self.coffee_factory.getCoffee(coffee_name)

class CoffeeFactory():
    coffee_dict = {}
    def getCoffee(self,name):
        if self.coffee_dict.get(name,False) == False:
            self.coffee_dict[name] = Coffee(name)
        return self.coffee_dict[name]
    def getCoffeeCount(self):
        return len(self.coffee_dict)

if __name__ == "__main__":
    coffee_factory = CoffeeFactory()
    # customer1 = Customer("Client 1",coffee_factory).order("coffee1")
    # customer2 = Customer("Client 2", coffee_factory).order("coffee1")
    # customer3 = Customer("Client 3", coffee_factory).order("coffee2")
    # customer4 = Customer("Client 4", coffee_factory).order("coffee3")
    # print("CoffeeFactory中coffee的实例对象数",coffee_factory.getCoffeeCount())
    print(coffee_factory.__class__.__name__)