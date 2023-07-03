# until this point we maintain our data as code in this 1main.py file by only instantiating 5 items
# now when we look to extend this application and add some more feature then we might have a 
    #-harder time to add those features because the actual data and the code are maintained in
    #-the same location(same 1main.py file) 
    
    # ? creating a database and maintain this information . but i want to keep things more simple 
    #- for the purposes of this tutorial 
    #- so will use csv(comma seperated values ) , each line will represent a single structure data
    #- csv is a great option here , becuase it allows the data to be saved in a table structured format
    #-  
       

import csv

class Item:
    pay_rate = 0.8 # The pay rate after 20% discount
    all = []
    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero!"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    # The problem is we are NOT going to have any instance on our hand to call this method
     #- form the instance because this method is actually designed for instantiating the object itself
    # so this means that this method could not be called from an instance so the way that this is 
     #-is going to be solve is by converting this method into a class method 

    # Now a class method that could be accessed in the following way .so it can be accessed from 
        #- class level only 
    # So this method should take full responsibility to instantiate those objects for us .
    # ? So how we will create a class method ,so for sure we need to delete self 
    # to convert this into a classmethod we need to use a decorator that will be responsible 
        #- to covert this method into a class method 
    # Now decorators in pyton is just a quick way to change the behaviour of the function the                 
    @classmethod
    def instantiate_from_csv(cls):
        # now we still recieve a parameter but it is named cls
        # the fact is when we call our class methods , THEN THE CLASS OBJECTS(Item) IS 
            #- ITSELF PASSED AS FIRST ARGUMENT ,ALWAYS IN THE BACKGROUND ,
            #- so its like instance which also passed as the first argument in the background
            #- self ~ cls   
        with open('items.csv', 'r') as f: 
            reader = csv.DictReader(f) # f: we passed the content of our file 
            items = list(reader) # convert the reader into a list 

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )




    # static method should do some work for you , that has a logical connection to a class .
        #- for example : if you want to check a number is an integer or a float ,then this is a good 
        #- candidate for creating a static method , because this has some connection to the class .
        #- so it makes sense to check if a price of an item has a decimal point .

    # NOTE : this means that this static methods are never sending in the background , the instance as
        #- a first argument and that is UNLIKE THE CLASS METHODS , THE CLASS METHODS ARE SENDING THE CLASS
        #- REFERENCE AS A FIRST ARGUMENT AND THAT IS WHY WE HAVE TO RECEIVE THE CLS . 
      # BUT WITH STATIC METHODS WE NEVER SEND THE OBJECT AS THE FIRST ARGUMENT . SO THAT IS WHY 
        #- WE SHOULD RELATE TO THE STATIC METHOD , LIKE A REGULAR FUNCTION THAT JUST RECEIVES PARAMETERS 
        #- like we are familiar with isolated functions .   
    @staticmethod
    def is_integer(num):
        # We will count out the floats that are point zero
        # For i.e: 5.0, 10.0
        if isinstance(num, float):
            # Count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"


# how to call static methods
print(Item.is_integer(5.0))     
# what is hapenning in the background : it is the fact that it enters here if isinstance(num, float):
    #- because it is integer it returns true 