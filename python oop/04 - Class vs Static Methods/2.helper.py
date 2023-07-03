# When to use class methods and when to use static methods ?

# STATIC METHOD : The only main difference between a class method and a static method is the fact that 
    #- static method are not passing the object reference as the first argument in the background 
    
# STATIC METHOD : We use static method when we want to do something that should NOT be unique per instance 
    #-  and the reason that you would like to create a class method is for instantiating instances from 
    #- some structure data that you own 
class Item:
    @staticmethod
    def is_integer():
        '''
        This should do something that has a relationship
        with the class, but not something that must be unique
        per instance!
        '''
    @classmethod
    def instantiate_from_something(cls):
        '''
        This should also do something that has a relationship
        with the class, but usually, those are used to
        manipulate different structures of data to instantiate
        objects, like we have done with CSV.
        '''

# THE ONLY DIFFERENCE BETWEEN THOSE:
# Static methods are not passing the object reference as the first argument in the background!


# NOTE: However, those could be also called from instances.

item1 = Item()
item1.is_integer()
item1.instantiate_from_something()