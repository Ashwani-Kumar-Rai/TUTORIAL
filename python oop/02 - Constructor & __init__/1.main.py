# For each item that i want to go ahead and create , i need to hard code in the attribute name 
    # eg:item2.name  # BEST PRACTICE IS TO AVOID THIS TYPE OF HARDCODING
    # WE CAN EXPLOIT THE FEATURE THAT INIT WILL BE CALLED EVERYTIME WE CREATE AN INSTANCE

# It could have been nicer ,if we call somehow declaring the class that that in order instantiate as
    # instance successfully name,price and quantity must be passed ,otherwise instance could not have been 
    # created successfully 

# it would have been a greate option if we can execute something in the background . 
    # SOLUTION : __init__ is CONSTRCUTOR ,ALSO CALLED MAGIC METHODS 

# Whenever you create an instance of a class then pyton executes this double underscore init function automatically    

class Item:
    def __init__(self, name: str, price: float, quantity=0): # default value of quantity is 0 
        
        # Assign to self object
        self.name = name # WE CAN DYNAMICALLY ASSIGN ATTRIBUTE TO INSTANCE FROM THIS MAGIC METHOD __init__
        self.price = price # DYNAMIC ATTRIBUTE ASSIGNING
        self.quantity = quantity

    # PROOF1
    # we don't need to pass price , qty seperately ,because self( object) is passed by default,which has all parameters
        # because we assign those attributes , once the instances has been created 
    def calculate_total_price(self): 
        return self.price * self.quantity


# Whenever you create an instance of a class then pyton executes this double underscore init function automatically    
item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)

print(item1.calculate_total_price()) # PROOF1
print(item2.calculate_total_price())


# you can add attributes to specific instances outside of constructor __init__ 
# item2.has_numpad = False