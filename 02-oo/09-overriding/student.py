class Customer:
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country


class ShoppingList:
    def __init__(self, owner):
        self.__owner = owner
        self.__items = []

    @property
    def owner(self):
        return self.__owner

    def __len__(self):
        return len(self.__items)

    def __getitem__(self, index):
        return self.__items[index]

    def add(self, item):
        if not item.can_be_sold_to(self.owner):
            raise ValueError()
        self.__items.append(item)

class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def can_be_sold_to(self, customer):
        return True

class AgeRestrictedItem(Item):
    def __init__(self, name, price):
        super().__init__(name, price)

    def can_be_sold_to(self, customer):
        if customer.age < 18:
            return False
        else:
            return True

class CountryRestrictedItem(Item):
    def __init__(self, name, price):
        super().__init__(name, price)

    def can_be_sold_to(self, customer):
        if customer.country == "Arstotzka":
            return False
        else:
            return True
        
customer1 = Customer("Alice", 25, "USA")
customer2 = Customer("Bob", 17, "Canada")
customer3 = Customer("Eve", 30, "Arstotzka")

item1 = Item("Regular Item", 10.0)
item2 = Item("Luxury Watch", 500.0)
item3 = AgeRestrictedItem("Alcohol", 20.0)
item4 = CountryRestrictedItem("Cultural Artifact", 200.0)

print("Testing can_be_sold_to method for Item:")
print("Item 1 can be sold to customer 1:", item1.can_be_sold_to(customer1))
print("Item 1 can be sold to customer 2:", item1.can_be_sold_to(customer2))
print("Item 1 can be sold to customer 3:", item1.can_be_sold_to(customer3)) 

print("\nTesting can_be_sold_to method for AgeRestrictedItem:")
print("Item 3 can be sold to customer 1:", item3.can_be_sold_to(customer1)) 
print("Item 3 can be sold to customer 2:", item3.can_be_sold_to(customer2))
print("Item 3 can be sold to customer 3:", item3.can_be_sold_to(customer3))

print("\nTesting can_be_sold_to method for CountryRestrictedItem:")
print("Item 4 can be sold to customer 1:", item4.can_be_sold_to(customer1))
print("Item 4 can be sold to customer 2:", item4.can_be_sold_to(customer2))
print("Item 4 can be sold to customer 3:", item4.can_be_sold_to(customer3))
