"""
Copy and paste rest of lesson here. 
"""

#Let's check a few more methods that exist on a string
my_name = 'quentin andre'
print(my_name.capitalize)
print(my_name.title())
print(my_name.count('en'))
print(my_name.replace('andre', 'smith'))
#Methods are natural ways of a) encapsulating functions that are relevant 
#to a type of object and of b) acting upon the object 

n_chars = len(my_name)
print(n_chars) # The number of characters in my name
#This is a function it is not called from within the object using the dot, it stands alone. 

my_upper_name = my_name.upper() #This is a methond. You are calling it with the dot, 
#from within the object, it is connected to my_name 

#What will this line do? 
print(my_name.lower()) # We reached inside the box for the method, but we did not run it yet. To call it, you need to add
#the () after. 

my_age = 39
print(my_age.numerator)
print(my_age.denominator) #These are properties that I can read directly 
print(my_age.as_integer_ratio) # Here, we reached for a method 
#If I want this method to run I need to call it. 
print(my_age.as_integer_ratio())

#Lets see a few more things about methods! 
greeting = 'Hello, welcome to class'
# next we are going to capitalize this greeting. 
print(greeting.upper())
print(greeting) # Still lower case, why?
#Most methods return a new value. Think of them as a machine that copies the 
#original, modifies it, and returns it to you. The original is not change. 
#Industry jargon, we say, the methods to not MUTATE the original object 

user_input ='quentin.andre@colorado.edu'
#My mission: Check that the email entered by the user is a .edu email 
bad_solution = user_input.endswith('.edu') # Returns false, white spaces are ruining everything 
#Multiple steps:
trim_input = user_input.strip()
print(trim_input)
good_solution = trim_input.endswith('.edu')
print(good_solution)
# Now can we find a better solution 
better_solution = user_input.strip().endswith('.edu')
#Comprehension check! 
is_this_true =user_input.strip.upper().endswith('.edu') #No because you capitalize the edu in list with upper() and then searched for '.edu'
This_is_true = user_input.strip.upper().endswith('.EDU')
is_this_true
This_is_true
#Could we do that
user_input.strip().upper().endswith('.EDU').print() # We can not do that since print() is not a method that 
#we can call on the resulting object 

#What about that?
user_input.strip().endswith('.edu').upper() #This won't work because the endswith is a boolean expression which can 
#only return True or False. The upper method does not exist on a bool object which is precisely what endswith will return. 

#Nice segue into some of the errors that can pop up 

user_input.shout()# AttributeError: When you attempt to reach for a method or property that does not exist 
#on an object of a certain type. 

my_age.denominator() # I am attempting to call a attribute as if it were a method 

#There are more than four different types of objects in Python 
#I'm going to show you how objects of different types are created. 

#First to create an int:
my_int = 10
#Or a string
my_str='Something with quotes'
#To create other objects, you need too call an object factory that will create the object for you.
#Here we will work with an object called decimal, that allows you to create decimal numbers with 
#exact representations (no floating point errors)
from decimal import Decimal #Trust me bro, not going to cover this one for now 

a = Decimal('.1') # Here I created a decimal object equal to .1. 
print(type(a))
b = Decimal('.2') #I am creating another decimal object. 
#Youo will recognize object factories from their capital letter. 
#Now that I have a new object, I can see what kind of methods and properties they contain. 
#With dot notation 
#What is the interest of this Decimal object
print(a+b)
print(a+b == Decimal ('.3'))
#An example of creating a new type of object and reaching for its method 