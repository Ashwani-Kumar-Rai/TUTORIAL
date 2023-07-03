# store management software

# we have our data starting with prefix item1 so that we know it is a related to each other 
# for python these are just 4 variable with different data-types
item1= 'phone'
item1_price =100
item1_qty = 5
item1_price_total = item1_qty * item1_price

print(type(item1)) # str
print(type(item1_price)) # int
print(type(item1_qty)) # int
print(type(item1_price_total)) # int

# For each of the type we also see the keyword of class
    # NOW THIS MEANS THAT THOSE DATA-TYPES ARE ACTUALLY INSTANCES OF STRING OR INTEGERS .
# <class 'str'>
# <class 'int'>
# <class 'int'>
# <class 'int'>
# SO IN PYTHON PROGRAMMING LANGUAGE EACH DATA-TYPE IS AN OBJECT THAT HAS BEEN INSTANTIATED 
    # EARLIER BY SOME CLASS .
# FOR THE ITEM1 VARIABLE , THAT HAS BEEN INSTANTIATED FROM A STRING TYPE OF CLASS NAMED 'STR'.   

# IT WOULD BE NICE IF WE CAN CREATE A DATATYPE OF OUR OWN . IT WOULD ALLOW US TO WRITE A 
    # CODE THAT WE CAN REUSE IN FUTURE EASILY IF NEEDED .

