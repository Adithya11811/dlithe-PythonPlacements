# write a python program to create a class representing shopping cart include methods for adding and removing items, and calculating total price
class ShoppingCart:
    def __init__(self):
        self.price = 0
        self.qty = 0
        self.items = dict()
        

    def adding_methods(self, price, qty, item):
        self.price+=qty*price
        self.items[item] = qty
        print("done adding")
        print()

    def removing_methods(self, price, qty, item):
        if self.items[item] < qty:
            print("There's not that qty of item u are trying to remove: \n")
            return
        self.price-=qty*price
        self.items.remove(item)
        print("removed successfully")
        print()

    def totat_price(self):
        print("The toatal price is", self.price)
        print("the items you purchased are",self.items)
        print()

print("\nWelcome to so-and-so store\n")
sp = ShoppingCart()
while(1):
    say = input("say add when u are adding items else remove :")
    item = input("Enter the item name: ")
    price = int(input("The price of the item: "))
    qty = int(input("Enter the qty u want: "))
    

    if say == 'add':
        sp.adding_methods(price, qty, item)

    else:
        sp.removing_methods(price, qty, item)

    t = input("If u want to check the total and all the item Y/N: \n")
    if  t.lower() == 'y':
        sp.totat_price()
        print()
    
    go_out = input("finished shopping y/n: \n")
    if go_out.lower() == 'y':
        break
    print()