print ('hello world') #In our python file, also called a python script. 
print('Hello friends')

# What are the big variable types in python? Hint, theres 34 of them. 
#String, float, int, boolian 
this_string = 'Quentin'
# I assigned the value 'Quentin' to the variable this_string
#This operation does not return anything 

this_float = 3.14 # this is a float 
this_int = 12 # This is an interger 
this_bool = False #Note the case sensitivity. 

#What can you do with variables 
#Only after the line is executed do you 
print(this_bool)  #Tab to auto complete the current selection 
print(this_string) # Tab again 
#what else can you print? 
print('hello') #you can print literal 
print(12) # you are not storing it in a variable, you are directly printing an output 
print(12+5) #Printing an expression 
#SKILL being able to 'trace the code' meaning, reconstruct te steps of a code 

#Another example of a expression
print(this_float + 5) # We can again trace the steps 

#What is print? 
#Print is a function, a function is a way of doing something in python 
#Functions are called using () 
#Functions take a number of argument s (whats inside here)
#Some functions take zero, others take many 

#How many arguments does print take 
#It can take one 
print(this_float)
#but it can take more 
print(this_bool,this_float, this_int)
#print is printing all of its arguments on the same line 

#LEt's do some calculations 
print(2+3)
print(2*5)
print(2+3*5)
print((2+3)*5) # PEMDAS

print(0.1 + 0.2)
print((0.1 + 0.2) == 0.3) #floating point error, operations with decimal numbers are by defualt, not exact. 

#How can we avoid floating point error? 
#One way is to round 
my_rounded_sum = round (0.1 + 0.2,1)
print(my_rounded_sum)
print(my_rounded_sum == 0.3) #this is now true 

#More logical comparisions 
print (1 < 2)
print (2 > 1)
print(1 >= 2)
print(1 <= 2)
print(1 != 2)

#you can also create more complex comparisions 
print(1 < 2) and (3 > 2)

condition_1 = True
condition_2 = True
condition_3 = False
condition_4 = False

print(condition_1 and condition_2) # True as defined

print(condition_1 and condition_3) # when using and, requires ALL conditions to be true 

print(condition_1 or condition_2) # True as defined 

print(condition_1 or condition_3) # when using or, requires AT LEAST ONE conditions to be true. 
#Very important! 

print(False + False)

print(True + True)

print(True == 1)

print(False * 5)

#lets get funky 
greeting = 'Hello' + 'world!' # The meaning of + changes when you apply it to a string. 

print(greeting)

laugh = 'ha' *3
print(laugh) #Here, means repeat when applied to a string
 

#When you want types to work nicely with each other, you will need to convert them first. 

#lets see type conversion 

my_age_as_a_str = ' 39 '
my_intro = "I'm Quentin and I'm "+ my_age_as_a_str

#A better way to do that is to convert one type to another using four neat functinos
#str()
#int()
#bool()
#float()
print(my_intro)

print(str(42))
#Is this really a string? 
type(str(42))

#Lets try others 
str(3.14)

#We can convert pretty much anything to a string, int, bool, or float 

#Let's try float 
float('Hello')
float('32')
float(False)
float(40)
float('fifteen')
#For float is going to work sometimes sometimes not. 

int('Hello')

int(False)
int(True)
int('32')
int(3.14)#Is this rounding or cutting of the decimal? 
int(3.9) # This confirms it is cutting off the deciamal 
round(3.9) #gives 4 not 3 
#Another great skill is running experiments on your code. 