#lets say I wanted to print all the squares between 0 and 1,000: 
#The way we did this so far was something like this: 
list_of_numbers = [0, 1, 2, 3, 4, 1000] #Not great 
#Its called range 
#in its basic form, range works like this: 
for i in range(1000): #It's the same thing as for i in [0, 1, 2, 3, ..... 999]
    print(i**2)
#It takes one argument called stop: The value at which you will stop. 
#You can also give two other arguments to range: start and step. 
for i in range (3,10,2):
    print(i)
#The start, stop, and step are thingsthat we've seen for slicing 
#They work in the same way for range, except that they create an iterable 
#rather than slicing the values in an exisiting iterable. 
for i in range (5, 30, 5):
    print(i)
#Now for something slightly more complicated. 
#Let's say we want to generate a list of all the squares of the numbers 1-9 
#We'll do that using a for loop first 
squares = []
for i in range (1,10): 
    square = i ** 2 
    squares.append(square)
print(squares)
#We built a list one element at a time, using a for loop 
#When you have to build a list (or any iterable) for another list (or another interable) 
#You will often encounter something called a LIST COMPREHENSION 
#Its simply a for loop, written in a more concise way, that builds a list. 

squares = [i ** 2 for i in range (1, 10)]
#A list comprehension starts with square brackets. after all, we're building a list. 
# Then an expression comes, here its (i**2) It tells us how each element of the list is going 
# to be constructed. 
#Then, comes the loop. FOR_STEP_VARIABLE. No colon, that's all. 
print(squares)

#Let's try another example. 
first_name = 'chase'
whats_this = [x.upper() for x in first_name]
print(whats_this)

#You can add another 'bell' to a list comprehension, an optional part of it 
#You can filter certain elements. 
#We want to get the squares of all the numbers between 0 and 9, but only
#if the square is less than 30. 

#This is the exact same list comprehension as before EXCEPT 
#We have an if statement, the if statement conditions whether an elements will be added
#to the list or not. If at a given iteration, the condition is 
#False, it is not added. If it is True, it is added. 
small_squares = [i ** 2 for i in range (0,10) if (i**2) < 30]
print(small_squares)

#Lets say you have a folder full of mess. You're working with a disorganized colleague 
#called Quentin. 

folder_content = ['data.csv', 'report.pdf', 'summary.csv', 'image.png', 'notes.txt', 'data2.csv', 'archive.zip']

#What we want, filter out all the elements that are not .csv files 
#Reminder, you can check if a file name ends with a .csv by using .endswith('.csv')
#Its a string method that returns true or false 
# Try to write a list comprehension that will return a list with only the csv files 

list_of_csv_files = [i for i in folder_content if i.endswith(".csv")]
print(list_of_csv_files)
