#Talk about collections
#Collections are different ways of storing things into a single variable 
#Up until now, when we were assigning content to a variable, we were assigning a single thing:
#EX) a = 'hello' 

#Now, we are going to learn (re-learn) how to handle assigning multiple values to a single variable 

# We are going to cover two kinds of collections today. The first kind is lists. 

my_empty_list =[] #Two square brackets 
#This is a list! 
type(my_empty_list) #New type of object! Now we know int, str, float, bool, decimal, list! 

#What can we do with lists? 
#Lists are what are called ORDERED COLLECTIONS OF ITEMS 
#So you can use it to store a sequence of other elements. 

my_favorite_numbers = [1, 2, 3, 4, 5] #You enter elements in a list by adding them
#between square brackets one at a time, separated by commas. 

#Lists can also contain strings 
my_favorite_colors = ['red', 'blue', 'green']

#Floats too! 
my_favorite_floats = [3.13, 2.718, 1.1618]

my_favorite_bools = [False, True, False] # Note that lists can contain
#repeated elements, they do not have to be unique! 

#You can also put different things in a list
my_mixed_list = [False, 3.14, 'Chase', 1, True]

#You can even put lists inside of lists 

my_list_of_lists = [[1,2], ['hello', 2], [False, 3.14]]

#You can really put anything you want inside of a list. 
#A list is, like most things in python, an object! 
#Meaning, lists are going to have...... methods! 

#Let's see what exists inside a list
my_favorite_colors # lets print it to remind us what's in there

#Lets check its methods
my_favorite_colors.append # Append is a method for adding an element, or several elements to a list 
print (my_favorite_colors.append('purple'))
#When you run the append method on the list, it does not return anything. 
#That's unlike what happens when you run a method on a string, it returns a 
#transformation of the string 

my_name = 'chase'
print(my_name.upper())

#So we ran a method on the list my_favorite_colors, and we did not get 
#anything in return, what happened then? 
print(my_favorite_colors) #That's strange

print(my_name) # It is in lower case because when we run a method on a string, 
#it returns a new string. It does not modify or mutate the original. 

#With the list, we saw aa mutation:
#After we ran the method append(), it changed the original content of the list 
#it did not return anything, it changed the original list. 
#It's mutated the original list 

#What would happen if we ran the method again? 
my_favorite_colors.append('purple')
print(my_favorite_colors) # Everytime you run append, it is adding additional content to the original list. 

#Lists are MUTABLE, meaning thheir methods modify them directly, they do not 
#return a copy of the list. They change the content of the list. 

#How would you add purple 50 times? You could run line 67 50 times, or create a loop like below. (remove
#the # if confused.)
    #for i in range (50):
    #   my_favorite_colors.append('purple')

# To know a list 
type(my_favorite_colors)
my_favorite_colors

#Let's learn another method on lists 
a = my_favorite_colors.pop() #Removes the last item eof the list and returns it. 
print(my_favorite_colors)
print(a)

#Now we've seen two methods, pop() removes the last one and returns it 
#append() adds something to the end of the lisit 
#One thing that we said wwas that lists are ordered 
#Because they ordered we can check what is located at a given position 
#in a list. This is called INDEXING. 

my_favorite_numbers = [ 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'] 
#To get the element located at a given INDEX in the list, 
#you can use [i] where i is the INDEX of the element that we want to get

my_favorite_numbers[0]#REMEMBER THAT PYTHON STARTS COUNTING AT ZERO 

#How would you get the fourth element on the list? 
print(my_favorite_numbers[3])

#8th?
print(my_favorite_numbers[8])

#What happens if we 
print(my_favorite_numbers[12]) #IndexError: Our list is shorter than that 

#how would i grab the last element 
#Complicated way: 
#How many elements are there in the list? 
n_numbers = len(my_favorite_numbers) #len is a function that tells you how many things are inside the collection 
my_favorite_numbers[n_numbers -1]

#There is a better way with a feature in python 
my_favorite_numbers[-1] 

#What do you think this will print? 
my_favorite_numbers[-2] # 2nd to last 

#That's called INDEXING: How we can grab a single element from a list? 
#Now lets get more ambitious: How do we grab multiple elements from a list? 
#We can use something called SLICING 
#Slicing works like this my_list[start:stop:step]
#Start tells you, where are we starting in the list? 
#Stop tells you where do we stop in the list? 
#Step tells you, how many items are we skipping? 

#Let's do a few examples 
my_favorite_numbers[0:5:1] #Grabs all the elements between index 0 and index 5 
#(exclusive) don't skip any 

my_favorite_numbers[1:4:1] #Grab all the elements between 1 and 4 (exclusive) don't skip any 

# lets see how skip works 
my_favorite_numbers[0:6:2] #all numbers between 0-6 exlusive, skip every other number 

# you can omit some oof these arguments when you slice 
#Demonstration 
my_favorite_numbers[0:5] # Which one was omited? The step! 
#Step, when omited, defaults to 1 

my_favorite_numbers[:6:1] # Start was omited
#Start when omited defaults to 0 

my_favorite_numbers[::1] # Start/Stop omitted 
#stops defaults to the length of the list 

my_favorite_numbers[::]# This will just give you the full list 

#one note: a slice returns a COPY of the list, meaning A NEW LIST. 
#why the copy matters
my_favorite_cities = ['Boulder', 'Paris']

lucas_favorite_cities = my_favorite_cities

print(my_favorite_cities) #This prints boulder and paris 
print(lucas_favorite_cities) #This prints boulder and paris 

#Now we visist Barcelona lets add it to our favorite cities 
my_favorite_cities.append('Barcelona')
print(my_favorite_cities) # Barcelona added 

#Lucas does the same but with Milan 
lucas_favorite_cities.append('Milan')
print(lucas_favorite_cities) # But Lucas didn't go to Barcelona, why is it there? 

#In writing this we said lucas_favorite_cites = my_favorite_cities
#I said lucas favorite cities and mine are defined by the list 
#Now, lets redo this with a small change 

my_favorite_cities = ['Boulder', 'Paris']

lucas_favorite_cities = my_favorite_cities[::] # This is creating a COPY OF THE LIST 

print(my_favorite_cities) 
print(lucas_favorite_cities) 

my_favorite_cities.append('Barcelona')
print(my_favorite_cities) 

lucas_favorite_cities.append('Milan')
print(lucas_favorite_cities) 

#Back to the main topic 
my_name ='Chase'
print(my_name[1:4]) #You can index and slice strings 
#Anything that is a collection and ordered, you can index. 

#Since lists are mutable, you can do more than reading their contents with indexing and slicing 
my_favorite_colors 
#Now lets say something common, NO I DON'T LIKE BLUE I LIKE PINK 

#where would we find blue in our list? Index one (spot 2)
my_favorite_colors[1]

#How would we replace it? 
my_favorite_colors[1] = 'pink'

my_favorite_colors
#We just placed 'pink' at the position one of the list, replacing blue 

#If you want to add something in the middle of the list, you can use 
#insert()

my_favorite_colors.insert(1,'gold')
my_favorite_colors

#Final thing, we can also swap multiple values at the same time 
my_favorite_colors[0:2] # We have a list with two elements, if we want we can subsitute two other elements 

my_favorite_colors[0:2] = ['yellow', 'orange']

my_favorite_colors
#What if the sequence that you are trying to substitue does not match the length of the original? 

my_favorite_colors[0:2] = ['black']
my_favorite_colors

my_favorite_colors[4:6] =['Cyan']
my_favorite_colors

#There is one more thing to show 
my_name ='Chase'

#We saw that, with a list, you can index and replace the value at that index:
my_name[0] = 'X' #STRINGS ARE IMMUTABLE
#You can only ever create a new one 
#You can read a string with indexing and slicing, never ever write to it. 

#Another type of collections called dictionaries (or DICTS for short)
#A dictionary is a collection of key-value pairs. 
#There are keys (words) that have values (definitions) much like a real dictionary 

#Here's the syntax to create a dictionary 
my_friends_age = {'Nick':40, 
                  'Sam': 35, 
                  'Juan':37} #Curly brackets, and inside, you put the key value pairs separated by commas 

#Unlike lists, dictionaries are not ordered. They simply match values to keys. 
#The values in a dictionary can be of different kinds: 
my_information = {
    'name' : 'Chase',
    'age' : 30,
    'hobbies' : ['hiking', 'dogs', 'running']
}

#For the keys you have more restrictions
#They are typically str, but sometimes int
#They must be unique
#They must be immutable objects 

#how do we use a dictionary? 
#Once you've created it, you can index it with a key 
#to know the value of that key
my_friends_age['Nick']
my_information['hobbies']

#Keys are case sensitive 

#What if we want to look for a key that doesn't exist? 
my_friends_age['Alice'] #KeyError: 'Alice'

#Dictionaries much like lists, are MUTABLE
#meaning, we can reach into them and update a value associated with a key. 

my_friends_age['Nick'] = 21 #We can reach into a dictionary with a key 
my_friends_age['Nick'] #We have updated the value associated with the key Nick. 

#What if we want to add our friend alice? 
my_friends_age['Alice'] = 50 # We simply name the key and assign it a value 
my_friends_age

#Dictionaries are also objects meaning that they have methods 
#Two useful methods. 
#Let's say that we're not sure if a dictionary has a key
#When we try to index with that key, we might get an error: 
my_friends_age['Nico'] #KeyError! 
#Errors aren't great because they stop your code. 
#Instead we can use a 'safe' method called get() 
my_friends_age.get('Nico',) #If they key exists it returns the value 
#if it doesn't it returns None. 

#If you want to delete a key from a dictionary 
#FUCK SAM ALL MY HOMIES HATE SAM
my_friends_age.pop('Sam') #Pop for a list takes a numerical index
#for a dictionary, it takes a key 
my_friends_age
#three methods to see what is inside a dictionary: 
my_friends_age.keys() #prints all the keys that exist
my_friends_age.values() #Prints all the values that exist 
my_friends_age.items() #prints all they key-value pairs 

#Final topic on dictionaries 
#Remeber how we learned that values can be anything? 
#Values can be dictionaries themeselves! 
#This is a very common data structure to represent users. 

my_friends_info = {
    #Master Dict: Keys are going to be user names. The values are going to be dictionaries containing information about
    #The user. 
    "Nick": {
        'age':31,
        'hobbies': ['basketball', 'cooking'],
        'city': 'Boulder',
    },
    "Sam":{
        'age':35,
        'hobbies': ['hiking', 'painting']
    }
}

#How do we use a more complex data structure like this? 
#How would you get all of nicks info? 

my_friends_info['Nick'] # What is the type of this object that we just got? 
#This is a dictionary 
#Let's double check 
nicks_info = my_friends_info['Nick']
print(type(nicks_info))

#So if this is a dictionary, how can we get nicks age directly from my_friends_info 

my_friends_info['Nick']['age']

#You know that you have a friend called Sam, but you're not sure if you have information about his hobbies. Can 
#you get his hobbies and none if this info is not recorded? 
#Hint: a method called get() is bound to dictionaries, it takes the key as an argument and returns none if they 
#key does not exist 

my_friends_info['Sam'].get('hobbies')

#What would happen if sam did not exist? Repalce sam with lisa
my_friends_info['Lisa'].get('hobbies')


#ITS THE FINAL EXERCISE 
#Nick recently picked up a exciting hobby: sourdough baking! 
#Can you add this hobby to nick's list of hobbies? 
#Hint lists have the .append() method bound to them that takes
#as argument the element that should be added to the list. 

my_friends_info['Nick']['hobbies'].append('Sourdough baking')
my_friends_info['Nick']

#Could I do that to add two hobbies in a row? 
my_friends_info['Nick']['hobbies'].append('Sourdough baking')
