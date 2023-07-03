# init method : a special method called init method ,that will construct objects for us .
    # In other programming languages it is called as constructor

    # init means initialize
    # syntax : def __init__(self): # we need atleast self as an argument 
    # now we can assign our car objects unique variables

         
# Note : We can re-use this class as a blueprint , to create more car objects
    #-we just call constructor and pass the new attributes's values

# SKELETEN OF CLASS 

# class Car:
#     make = None # attributes or variables
#     model =None # attributes or variables
#     year = None # attributes or variables
#     color = None # attributes or variables

#     # self refers to the object that is using this method 

#     def drive(self):# methods or functions 
#         print("This car is driving")
#     def stop(self):# methods or functions
#         print("This car is stopped")    


class Car:
   
   # we can recieved arguments when we create car objects, but we need to pass them as agguments
        #-to our init method  
   # when we recieved these arguments,we can assign them to each car's specific attributes
        #-but we need to preeced them with self,(self refers to the object that we are currently
        # -working on  )   

    # Notice we are havind 5 argument but we are passing only 4 arguments
        # we don't need to pass anything for self it is passed automatically


    # class variable : is declared inside the class,but outside the constructor
        # we can set some default values for some variables
    wheels = 4     #class variable 
    # whenever we create a car object, we can pass unique make,model,year,color
        #-But we will always have  this wheels=4 (for all the objects)
    # But each object will have copy of this variable(wheels=4) so we can change it.
    


    # each object can have their unique values assigned to these insatance variables
    def __init__(self,make,model,year,color): # init method or constructor
        self.make = make #instance variable   #self.make = (whatever make that we recieve) make 
        self.model =model   # instance variable
        self.year = year    # instance variable
        self.color = color # instance variable
   

    # Note : think of self as replacing the self with the name of the object we are working on
        # In this case self will be replaced by car_1,car_2 , depending on which object we are
            #-working on    
    def drive(self):
        print("This "+self.model+" is driving")
    def stop(self):
        print("This "+self.model+" is stopped")    



    # Now we can start creating some car objects in file 40    






         


