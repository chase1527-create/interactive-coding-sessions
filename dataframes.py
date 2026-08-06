import pandas as pd

#Let's write a dictionary 
data = {
    "Month": ['January', 'Feburary', 'March', 'April'],
    "Marketing_Spend": [5000, 7000, 6000, 8000],
    "Sales_Spend": [2000, 3000, 2500, 4000],
    "Leads_Generated": [150, 200, 180, 250]
}

#This dictionary is not a dataframe, but it is a very good mental model 
#for thinking about dataframes:
#The columns are like keys in a dictionary. 
#And the values are arrays/lists that all have the same number of elements. 
#They correspond to the rows 

#In fact, a very common way of creating a dataframe by hand
#Is to create it from a dictionary: 
df = pd.DataFrame(data)
print(df)

#As you might guess, it is pretty uncommon to type the values, one by one into python. What is much more
#common is to read the content of a file into a dataframe 

df = pd.read_csv("sales_data.csv") # Relative path

#The first thing you do is inspect your data 
print(df)
#If you print a large enough dataframe, your terminal will crash. 
#a better way is to print the first or last few methods of a row 

print(df.head())  # First 5 rows
print(df.tail()) # Last 5 rows 

#2nd inspection
df.info()

#If you nejed to access each of these info individually, you can: 
print(df.columns)
print(df.index)
print(df.shape)
print(df.dtypes)

#Actually working with Dataframes
#You can read the contentj of columns in your data by indexing 
print(df['Month']) #Individual columns in dataframes are called Series 
print(type(df['Month'])) #Series are like arrays, with an index in front. 

#You can also ask for multiple columns: 
print(df[['Month', 'Sales_Spend']]) #We index with a list of column names 
# You get a dataframe 

#Again, repeating some content 
#You can read with indexing 
#And you fcan assign values with indexing 

#Exercise 1 increase the sales_spend by 100 (+100) and save it to the dataframe
df['Sales_Spend'] = df['Sales_Spend'] + 100 # Here we are getting the content of the column 
#Modifying it and putting it back into the dataframe. 
print(df['Sales_Spend']) 

#What is new iis that we can also use indexing to create new columns 
#Let's say we want to calculate the cost per lead: 
print(df['Marketing_Spend'] / df['Leads_Generated'])

#How do we add these values to a column in the dataframe? 
df['Cost_Per_Lead'] = df['Marketing_Spend'] / df['Leads_Generated']
print(df.head())

#Another common operation is to filter the dataframe 
#Let's say we want to see whcih months were particualarly effective 
#in acquiring leads. We want to see on which months the costs of 
#acquiring leads was less than 15. 

#Let's create a mask, something that for each row contains true or false, depending on whether cost
#per lead was < 15
mask = df['Cost_Per_Lead'] < 15
print(mask) 

#The next step is to apply the mask:
print(df[mask])

#Wait what? 
# We've used df[index] both to index columns (using a column name or list of names)
#but also df[mask] to index rows (using a mask)

#Fortunately they later introduced a more correct and intuitive way 
#of indexing dataframes: 

#the syntax is df.loc[row_index, col_index]
#Let's say I want to see all the rows, and just the columns Marketing_spend and #Sales_spend
print(df.loc[:, ['Marketing_Spend', 'Sales_Spend']])

print(df.loc[[0, 2, 4], ['Marketing_Spend', 'Sales_Spend']]) #Just line 0, line 2, line 4 with the same columns
#It's like indexing a matrix, execpt we are using the name of the rows
#and the name of the columns

print(df.loc[:, 'Sales_Spend'])

#1. Always use .loc to index a dataframe 
#2. Remember that the first indexer is ROWS, the second is COLUMN 
#3. Remember that we are using the NAMES of the rows and columns, not their position
#To index them (or a mask)

shorter_df = df.loc[[5, 6, 7], ['Marketing_Spend', 'Sales_Spend']]
print(shorter_df.loc[5, :])

#Skill 2: Summarizing Dat
#Both Dataframes and series have methods. You can use them to get the mean(), the min(), the max() etc

print(df.loc[:, 'Cost_Per_Lead']) # Here I get a series
print(df.loc[:, 'Cost_Per_Lead'].mean())

print(df.loc[:, ['Sales_Spend', 'Marketing_Spend']]) # This gives me a dataframe with two columns
print(df.loc[:, ['Sales_Spend', 'Marketing_Spend']].mean())

#When you call a method to summarize a dataframe with numeric columns
#You are getting one vlaue per column. Here, we get the average marketing spend
#and the average sales spend, taken across all the rows.

#Now consider this second example:
print(df.loc[:, ['Sales_Spend', 'Marketing_Spend']].sum(axis=1)) # This time, I want to get the sum of
#the Sales_Spend and the Marketing_Spend, but not at the column level, I want them at the
#row level. I want to know, for each month, and how much we spend in sum
#on marketing and sales combined

#To sum across the columns, we eed to set axis = 1
#Much like on matrices 
df["Total_Spend"]

print(df.head())

#Great Job, we did some basic data cleaning and manipulation with pandas 
#Last step is to save our dataframe back into a file:
df.to_csv("sales_data_cleaned.csv", index= False) # Thanks but no thanks no index 