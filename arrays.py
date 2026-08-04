#Before we begin working on arrays we are going to import a library 

import numpy as np
import math
# You reach into a library by using dot notation:
print(math.pi)
print(math.sqrt(9))

#lets create our first array together 

my_array = np.array([1, 2, 3, 4, 5]) #We are using the function with a single argument, (1,2,3,4,5)
print(my_array)

#Looks a lot like a list, it contains elements in order. We can index it. 
print(my_array[0])

#we can slice it: 
print(my_array[0:3])

#So what's the difference 

#First difference, arrays can only contain elements of the same type. (no strings, int, float combos)
my_list = ['Quentin', False, 35]

print(type(my_list[0]))
print(type(my_list[1]))
print(type(my_list[2]))

#Now do it in an array and see what happens 
my_array = np.array(['Quentin', False, 42])
print(my_array)
print(type(my_array[1]))

#All the elements were converted to strings. Why? 
#Because arrays require all its elements to be of the same type. 
#When we create an array with multiple types, they all get converted (coerced) to a single 
#compatible type. 

#Because arrays only contain a single type, they have what is called a data type or D-Type for short
print(my_array.dtype) #Property called dtype. 

int_array = np.array([1, 2, 3])
float_array = np.array ([3.14, 2.76, 1.12])
bool_array = np.array ([False, True, True])
print(int_array.dtype)
print(float_array.dtype)
print(bool_array.dtype)

#Arrays have a dtype, that conditions what lives inside of them. 

#2nd difference between lists and arrays 
#Arrays have a fixed size, something called a shape. 

my_list = [1, 2, 3, 4, 5]
my_list.append(6)
print(my_list)
my_list.pop(0)
print(my_list)
my_list.pop(0)
print(my_list)
#The length of my list changed multiple times. 
#It makes sense because lists have a lot of methods to add or remove elements. 
#We have pop(), append(), insert()....

my_array = np.array([1, 2, 3, 4, 5])
my_array.append(6) # Creates an error 
my_array.pop()
# You can not change the length of an array. 
# You can not add or remove elements from the array. 

# What you can do is create a new array, with additional elements 
my_bigger_array = np.append(my_array, 6)
print(my_bigger_array) # We now have a bigger array but the original array has not changed. 
print(my_array)

#Let's see what we can do with arrays that we could not do with lists: 

#Suppose we sell five products. I'm going to write down their prices 
#and quantities sold: 
prices = [9, 19, 4, 14, 25]
quantities = [120, 75, 300, 50, 40]
#P and Q for 5 different products 

#Let's forgot about arrays for a minute. Let's work with lists.
#I would like you to calculate for each of the five items
#The total revenue : Price x Quantity

revenues = []
for (p,q) in zip(prices, quantities):
    r = p * q 
    revenues.append(r)
print(revenues) # this results in a list containing the revenuses for the 5 items 

#This results into something like this 
arr_price = np.array(prices)
arr_quantities = np.array(quantities)
#Now this is where the magic happens 
arr_revenues = arr_price * arr_quantities
print(arr_revenues)

#Python understands that you want the element wise product of these two arrays. 
#This operation is much simpler to write and is blazing fast compared to a loop. 
#this is because, under the hood, python knows the type and shape of the arrays. 
#and does not have to do a lot of checks it would normally perform. 

#Numpy implements 'vectorized' operations that allow computers to work much faster. 
#Let's see a few other examples showing how much nicer it is to work with arrays 

#Sales for five products in two months. 
sales_jan = np.array([120, 75, 300, 50, 40])
sales_feb = np.array([110, 60, 330, 80, 25])

#How much more did we sell in Jan compared to feb 
diff = sales_feb - sales_jan
print(diff)

#By how much did the sales grow between Jan and Feb? 
growth_rate = sales_feb / sales_jan
print(growth_rate)

whats_this = sales_feb == sales_jan
print(whats_this)
whats_this_again = sales_feb >= sales_jan
print(whats_this_again)

#What else can we do with arrays? Numpy contains a bunch of functions that can be applied to arrays, for instance
np.sqrt(sales_jan) # Square root of all the Jan sales 
np.exp(sales_jan) # Expoenetial of all the Jan sales 

#Arrays have methods too! 
sales_jan.mean() # average sale volumn across the 5 items 

#What can go wrong when working with arrays 
five_prices = np.array([1, 2, 3, 4, 5])
four_quantities = np.array([1, 2, 3, 4])
four_quantities * five_prices # Results in an error, to be added, multiplied, divided, compared, etc
#Arrays need to have compartible shapes: 
print(four_quantities.shape)
print(five_prices.shape)

#Other common hiccup 
str_arr = np.array(['A', 'B', 'C', 'D'])
str_arr + four_quantities #Also results in an error due to incompatible dtypes 

#Quick refresher on indexing: 
#We can use indexing to access a value: 
arr_prices = np.array([5, 10, 15, 20, 25])
print(arr_price[0])
arr_price[0]

#We can also use indexing to replace a value 'in place'
arr_price[0] = 20 
print(arr_price)

#We can also use slicing to access values:
print(arr_price[0:3])
#... and to replace values
arr_price[0:3] = [7, 14, 21]
print(arr_price)

#these two behaviors are common to lists and arrays. 
#With arrays you can do two more things 
# 1. Boolean Indexing, or Masking 

arr_price = np.array([7, 14, 21, 20, 25])
mask = [False, False, True, True, False]
print(arr_price[mask]) # I am using square brackets, and using the mask as an index

#All the elements that had a False, in front of them were omitted. And the only 
#elements that had a true in front of them were returned by the indexing. 

# I'm going to show a useful examples of how these masks and Boolean indexing is used. 

#Example 1
arr_q = np.array([10, 20, -5, -2, 4, 10]) # It is obvious that this array contains errors 
#You can not sell negative items. 
#Now imagine we have 1,000 quantities like this. We cannot inspect by hand 
#which ones are negative, how could we use a mask to flag all the negative values? 

#1. Create a mask that identifies the negative values
#2. Use the mask to index all the negative values in the array.

mask = arr_q < 0 # comparing the whole array at once builds the boolean mask for you
print(mask) # [False False  True  True False False]
print(arr_q[mask]) # [-5 -2] the negative values, pulled out using the mask
#Our mask is False, False, True, True, False, False 
#When we put it in front of our dataset we get [-5, -2]

#We used the mask to see exactly which quantities were less than 0 

#3. Can we fix these errors? Can we use this mask to replace all the negative quantities with 0 instead?

mask = arr_q < 0
arr_q[mask] = 0 #Remember that you can use indexing to read or replace values. 
print(arr_q) # [10 20  0  0  4 10] the negative values have been replaced with 0

#Bonus one liner
arr_q[arr_q < 0] = 0 # Indexing arr_q using the mask (arr_q < 0), then assign the value 
#0 to all these indices. 

bakery_visits = np.array([0, 15, 12, 8, 9, 0, 5]) # These are the visits to a bakery Mon-Sun

#1. How many visits did the bakery get per day on average? Hint use the mean() method
print(bakery_visits.mean()) # On average, our bakery is getting 7 visits per day 

#2. Are there any days where the bakery did not get any visits? Show them using an index.
no_visits_mask = bakery_visits == 0
print(no_visits_mask) 

#3. Excluding the days where the bakery did not get any visits, how many visitors did the bakery get?
# Hint, use the mean () method again.
print(bakery_visits[~no_visits_mask].mean())

# the 2nd thing you can do with arrays and not lists is much simpler 
#also has a cool name "fancy" indexing

arr_words = np.array(['The', 'quick', 'brown', 'fox'])
#Fancy indexing simply means: giving a list of indices that you want the value of. 

desired_indices = [0, 1, 3]
arr_words[desired_indices] # I index using a list of positions of indices I want. 

#You can also repeat positions 
desired_indices = [0, 1, 3, 0, 1, 2]
arr_words[desired_indices]

#Whats the use of fancy indexing? 
#Most commonly used for randomly selecting rows in a dataset. 

#Exactly like indexing, but you can use a list of numbers rather than just one. 
# You can also skip the variable definition 
arr_words = [[0, 1, 0, 1, 3]] # Note the double bracket, the first one is to say "I'm indexing"
#The second one to say 'this is a list of indices' 