import numpy as np 

#Reminder, this is an array: 
one_d = np.array([1, 2, 3, 4, 5])

#You might remember that arrays have a shape: 
one_d.shape

#We are going to create our first 2D array 

two_d = np.array(
    [[1, 2, 3],
    [4, 5, 6,]]
)
print(two_d)

#I see two lines, corresponding to the number of sublists 
#and three columns, corresponding to the number of elements in each sublist. 
#If the sublists do not have the same number of elements, 
#You are going to get an error. 

#Now we have a 2D array, lets look at its shape 

print(two_d.shape)

#When you have a matrix the first element of the shape is always the number of ROWS 
#The 2nd is the number of columns 

#ROWS COLUMNS, ROWS COLUMNS, ROWS COLUMNS 

#A 2D array is an array 
print(type(two_d))
print(type(one_d))

#They are going to work in extremely similar ways to one dimensional arrays 
#One term that you might see so It's being given 
#1D array is a VECTOR 
#2D array is a MATRIX 
#a single element is a SCALAR

#Scalar (single), Vector (2D), Matrix (3D) but only vector and matrix are arrays

#OK, so if 2D arrays are arrays, we can probably index them. 
#Let's see how that works 
print(two_d) 
print(two_d[0]) # If you give a single index to a matrix, you get the row 
# corresponding to that number 
print(two_d[-1]) # This is printing the final row of our matrix 

#We can also do slices on 2D arrays 
print(two_d[0:2]) # This is only returning the first two rows of our matrix, our matix happens to 
#only have two rows 
print(two_d[0:1])

print(one_d) # A small but important aside 
print(one_d[0]) # only one element a scalar 

print(one_d[0:1]) 

#Now back to 2D arrays: 
print(two_d[0]) # A 1D array 
print(two_d[0:1]) # A 2D array with just one row 

#So what about columns now? 
#When  we index a 2D array with a single number, we are getting a single row
#When we index a 2D array with a single slice, we are getting a subset of the rows 

#How do we slice and index on columns ? 
print(two_d[0,0]) # This means: Row 0, Column 0 
print(two_d[1,2]) # This means: Row 2, Column 3 

print(two_d[-1, -1])

#What if you want all the rows? 
print(two_d[:,1]) #this means ALL of them 

print(two_d[:, 0:2])

#Let's say we want the first column of the first row: 
two_d[0][0] # This would be used in lists, using this with arrays gets complex and unnecessary 

two_d = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

#Exercise 1: Using indexing, replace the element 5 by 999
two_d[1, 1] = 999
print(two_d)

#Exercise 2: Replace the final column by [7, 14, 21]
two_d [:, 2] = [7, 14, 21] 
print(two_d)

#Final exercise Double the values in the first row 
two_d [0, :] = two_d[0, :] * 2
print(two_d)

two_d = np.array([
    [1, -2, 3],
    [-4, 5, -6],
    [7, -8, -9]
])
#Exercise 4 replace all the negative values with 0s
#a) write a mask matrix that contains true where all the negative values are in two_d
mask = two_d < 0

#b) Use the mask to print all these negative values
print(two_d[mask])

#c) Use the mask to replace the negative values by 0s
two_d[mask] = 0
print(two_d) #We are replacing the negative numbers by zeros in the original matrix 

#We said on Tuesday that the main benefits of arrays is that you can add, multiply, subtract, divide them
#As long as they have compatible shapes 
#The same is true for matrices because they are arrays 

a = np.array([
    [1, 2],
    [3, 4]
])

b = np.array([
    [1, 1],
    [2, 4]
])

print(a+b)
print(a-b)
print(a/b)
print(a*b)

#Same as Tuesday, this is the main benefit of matrices 

#2D arrays have the same methods as 1D arrays, with a very small twist 

#How many products of A, B ,C were sold in months Jan - April
units_sold = np.array([
    [120, 150, 130, 170],
    [76, 60 , 90, 80],
    [300, 330, 310, 350]
])
print(units_sold)

#You probably remember that arrays have methods like sum(), mean(), min(), max() 
#What happens if we do: 
print(units_sold.mean())

#The mean of all product sales across all months and all products 
#When you have the matrix data, it can be nice to get the means by rows
#and by columns instead. Means by rows would mean: 'Average sales of each product
#Across the four months, means by columns would mean 'Average sales for each month 
#across the three products 

#How can you do that? 

#The methods have a magic keyword called axis
#Axis tells you on which axis you are summarizing 

print(units_sold.mean(axis=0)) # It means we average across the axis 0, which are the rows
# The rows are going to disappear, and we will have mean per column 
#If instead, we do 
print(units_sold.mean(axis=1))

#The axis specifies the axis that will disappear. On which the method will be applied. 

#Exercise 1 The method min() gives you the minimum of an array. Use this method to find the smallest amount sold
#across the 4 months for each of the 3 products
print(units_sold.min(axis=1))

#Find the largest cell generated for any product across the four months:
print(units_sold.max())

#Final one: Fine the largest sale for product A: 
print(units_sold[0].max())