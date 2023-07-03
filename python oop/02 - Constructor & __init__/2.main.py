# BELOW two points make of init powerfull
# 1> name: str  ,,,object reference to the class of str ,then it will accept string only 
# 2> NOTE : quantity=0 , when we set the default value to integer , it made the quantity an integer variable
class Item:
    def __init__(self, name: str, price: float, quantity=0): 
        # Run validations to the received arguments , if the below conditions fail it will throw assertion error
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero!"
        # assert is a statement keyword that is used to check if there is a match between ,what is hapenning
            # to your expectations  
        #  after comma the string f"Price {price} is not greater than or equal to zero!" is a modified assertion error

        # Assign to self object
        self.name = name
        self.price = price 
        self.quantity = quantity

   
    def calculate_total_price(self): 
        return self.price * self.quantity

# Problem
# what will happen if we pass string inplace of int
item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3) # 100010001000 it multiplies string 1000 three times
# ONE WAY: in __init__ declare name is a string etc 

print(item1.calculate_total_price()) 
print(item2.calculate_total_price())


