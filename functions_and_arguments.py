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