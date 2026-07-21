#We have seen many functions already 
print('Hello World')
print(len('Hello'))
print(abs(-7)) # returns the absoutle value of a number
print(str(3.14)) 

#What we're going to do is dissect what functions are doing, and what they are. 
#A function is like a machine. It typically takes inputs (between 0 and many),
#It is running commands, doing things. And most often it RETURNS something to the userr. 

#You can think of most functions as a conveeyer belt. 

#If I use the len function ():
my_str = 'Hello World'
len_of_my_str = len(my_str) # Takes a single argument, here a string 
#Returns to the user the length of that string. 
print(len_of_my_str)
#A function that returns something is useful, because it gives you something back that you can store into a variable and reuse 
#for other purposes later 

#Not all functions are like that. 
#Others are more like engines. They take inputs (gas and O2) they do things, but they do not return anything to the user. 
print('Hello World') #Everytime I run t his, it is going to print to the REPL 
what_is_this = print('Hello World') #Execute the function print('hello world')and 
#store whatever it returns into the what_is_it_variable.
what_is_this #That's odd, it does not show anything 
print(what_is_this) #It prints 'None'
#There is nothing in what is this 

print(2 + 3) # If I 'run this, I will see 5 
my_result = print(2+3)
print(my_result) #Contains None, again, print does not return for anything 

#one last thing we need to know about functions before we practice writing them 
#Functions take arguments, we can supply the arguments to the functions in two different ways 
#1. By position
print(round(3.14,2)) # The first argument is the number to be rounded. 
# The second is the number of digits after the decimal you want. 
#The order matters: 
print(round(1,3.14))#An error 
#The second way is to include named arguments 
#Do you remember the print fucntion? 
print('A', 'B', 'C', 'D') #You gave it many arguments in sequence. 
#and it will print them all 
#The print function also takes 'secret' arugments that have defualt values 
#Meaning when you do not specify them, they already have a default value

print('A', 'B', 'C', 'D',sep='*')
# another one:
print('A', 'B', 'C', 'D', sep= '*', end ='!')
#One final thing: you can use names to eliminate all 
#ambuguity about positional arguments:
round(number=3.14, ndigits =1)
#This is the same thing as round(3.14, 1)

#Let's practice writing our own functions now. 
#We write functions when we want to have a list of actions
#that we can easily reuse in different places 

#Create a function that can calculate a price increase
#when given a rate 

#We say that we define a function: 
def show_price_increase(base_price, rate_increase):
    #The body of your function is what will happen everytime the function is called. \
    new_price = base_price * (1 +rate_increase)
    print(new_price)
    #We are now done, we press shift + enter to define our function (highlight)
#Now that the function exists, we can call it! 
show_price_increase(10, .1)
show_price_increase(30, .2)
#What kind of function did we create here? A conveyer belt? or an engine? 
#We are making an engine, the function is not RETURNING ANYTHING
new_price = show_price_increase (10, .2)
print(new_price)

#How can we modify our function to return a value 
#We say that we define a function: 
def calculate_price_increase(base_price, rate_increase):
    #The body of your function is what will happen everytime the function is called. \
    new_price = base_price * (1 +rate_increase)
    return new_price # This is what you had back to the user. 
    #We are now done, we press shift + enter to define our function (highlight)

my_new_price = calculate_price_increase(5, .25)
print(my_new_price) # This time we got something back, that we could store into a variable. 
#Whatever happens inside a function is LOST after the function is done running. So if 
#you want to get it back, ask the function to return it. 

#One final thing with functions
def show_total(price, quantity):
    print('Starting to calculate the price...')
    total = price * quantity
    return total # Engine or convyer belt? If there is a return = convyer belt
    #After return, functions job here is done. Any line after a return will never be executed. 
    print('Finished calculating the price')

total = show_total(.99, 10)
