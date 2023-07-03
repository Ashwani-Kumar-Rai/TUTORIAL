# CLASS ATTRIBUTE : IS AN ATTRIBUTE THAT BELONGS TO THE CLASS ITSELF ,
    # YOU CAN ACCESS CLASS ATTRIBUTE FROM INSTANCE LEVEL ALSO 
# CLASS ATTRIBUTE : IN THIS FILE , ALL BEFORE INSTANCE ATTRIBUTES
# Consider a sitaution that you'll want to make use of an attribute that is going to be global
    # or across all the instances now are a good candidate , for example discont
    # this attribute is going to be shared across all the instances  

class Item:
    pay_rate = 0.8 # The pay rate after 20% discount

    # now we need to figure out how we are going to add our instance for each time that we are going 
        #- going to create an instance , HINT : USE __init__
    all = [] # empty list 
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
        # self.price = self.price * Item.pay_rate
        self.price = self.price * self.pay_rate

    #can we change the way object is reporesented in this list here 
        # __repr__ : magic method inside our class
        # __repr__ : change the way we represent our objects 


    def __repr__(self): # This  list is way more friendly then previous one 
        return f"Item('{self.name}', {self.price}, {self.quantity})"


item1 = Item("Phone", 100, 1)
item1.apply_discount()
print(item1.price) #80.0

item2 = Item("Laptop", 1000, 3) 
item2.pay_rate = 0.7 # to assign a discount to a particular item and not all item 
# what will happen here : for item2 ,it will find the attribute of pay rate in the instanc level 
    #- so it does not really have to go ahead to the class level and bring back the value of pay rate
# for item1 : it is still going to read from the item level which is going to be 0.8    
item2.apply_discount()
print(item2.price) # 64.0

item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)
 
# Reference of class level itself , i am not going to create an instance 
print(Item.pay_rate) 
print(item1.pay_rate) 
print(item2.pay_rate) 
# we need to understand something when we work with instances in python 
    # so when we have instance in our hand ,then at first this instance tries to bring the 
        #- attribute from the instance level at first stage, but if it doesn't find there 
        #- then it is going to try to bring that attribute from the class level . 
    # so what does that means it means that item1 did something here 
        #- okay so i don't have this attribute right in here because that is just not an attribute 
        #- that is assigned to me . so i'm going to search that from the instance level then i am going
        #- to find it and print it back ,that is exactly what is happenning here
    
    # item1 and item2 are instances that could not find the pay_rate attribute on the instance level
        #-so both of them went ahead and try to bring this attribute from the class level 
        #- and since it really exists in class level, we were able to access those      

print(Item.all) # we have 5 element 

for instance  in Item.all:
    print(instance.name)


# BUILD IN MAGIC ATTRIBUTE , A MAGIC METHOD THAT YOU CAN GO AHEAD AND SEE ALL THE ATTRIBUTE 
    #- that are belonging to that specific object ,and that is achieavable by double underscore 
print(Item.__dict__) # all the attributes for class level



print(item1.__dict__) # all the attributes for instance level 
# this will go ahead and try to bring you all the attributes that are 
    #- belonging to the object that you apply this attribute and want to 
    #- see its content