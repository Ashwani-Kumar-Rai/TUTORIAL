# OBJECT AND INSTANCE ARE SYNONYMS
# THIS CLASS WE DEFINE VARIABLE AND FUNCTIONS : SO THAT WE DON'T HAVE TO MANUALLY CREATE SAME VARIBALES
# USE PASS AT THE BEGINING TO MAKE THE STRUCTURE OF PROGRAM , THIS WILL STOP ERRORS 

# How to create a class:
class Item:


# how can we design some methods that are going to be allowed to execute on our instances
    # this medthod will be accessible from our instances 
    def calculate_total_price(self, x, y): # when this method was called , self was passed in the background
        # Python passes the object itself as the first argument ,when you go ahead and call those methods
        # when you call a method from an instance(item1.)
        # python passes the object itself as the first argument every time 
        # So , that is why we are not allowed to create methods that will never recieve parameters 

        # Eg Error : def calculate_total_price():
            #  calculate_total_price() takes 0 positional argument but 1 was given 
        # what this error says : python tries to pass one argument and you are not receiving any parameters   
            # that is why you always have to recieve atleast one parameter when you go ahead and create your 
                # methods
        # because we always recieve these parameters it sa common approach to call these parameters as self         
    
        return x * y # METHODS    :ARE FUNCTIONS THAT ARE INSIDE CLASSES 
                     # FUNCTIONS  :ARE STANDALONE PIECE OF CODE OUTSIDE CLASS 


# HERE ,WE ACTUALLY HAVE A RELATIONSHIP BETWEEN BELOW 4 LINES OF CODE , BECAUSE EACH ONE OF THE 
    # ATTRIBUTES ARE ASSIGNED TO ONE INSTANCE OF THE 
# How to create an instance of a class
item1 = Item()
# Assign attributes:
item1.name = "Phone"
item1.price = 100
item1.quantity = 5

# Calling methods from instances of a class:
print(item1.calculate_total_price(item1.price, item1.quantity))


# How to create an instance of a class (We could create as much as instances we'd like to)
item2 = Item()

# Assign attributes
item2.name = "Laptop"
item2.price = 1000
item2.quantity = 3


# WE HAVE A DATATYPE OF ITEM HERE , WE HAVE CREATED OUR OWN DATA-TYPE
print(type(item1)) # <class '__main__.Item'>       # THIS IS DIFFERENT COMPARED TO EARLIER
print(type(item1.name)) # int
print(type(item1.price)) # int
print(type(item1.quantity)) # int



# Calling methods from instances of a class: 
print(item2.calculate_total_price(item2.price, item2.quantity))


# random_str="aaa"
# print(random_str.upper()) # we have some methods that we can execute for each of our strings 
# we grabbed an instance of a string that i named str , and in the next line i executed the upper method  
