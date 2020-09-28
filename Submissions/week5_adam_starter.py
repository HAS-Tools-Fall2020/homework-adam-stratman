# Example solution for HW 4

# %%
# Import the modules we will use
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# %%
# ** MODIFY **
# Set the file name and path to where you have stored the data
filename = 'streamflow_week5.txt'
filepath = os.path.join('../data', filename)
print(os.getcwd())
print(filepath)




# %%
#Read the data into a pandas dataframe
data=pd.read_table(filepath, sep = '\t', skiprows=30,
        names=['agency_cd', 'site_no', 'datetime', 'flow', 'code']
        )

# Expand the dates to year month day
data[["year", "month", "day"]] =data["datetime"].str.split("-", expand=True)
data['year'] = data['year'].astype(int)
data['month'] = data['month'].astype(int)
data['day'] = data['day'].astype(int)

# %%
# Sorry no more helpers past here this week, you are on your own now :) 
# Hints - you will need the functions: describe, info, groupby, sort, head and tail.


# %%
# answering question one of homework 
# checking out the first entries of data
print(data.head(10))
# checking out the last data entries 
print(data.tail(10))
# Seeing what "data" is comprised of 
print(data.info(10))

# chacking the shape of the data 
print("number of rows, number of columns in data", data.shape)
# %%
# checking statistics of entire data 
print(data.describe())
# %%
# looking at flow statistics for entire dataset
data[["flow"]].describe()
# %%
# statistics of each month concerning flow 
data.groupby(['month'])[["flow"]].describe()

# %%
# looking at five smallest/highest flow values for entire set of data using data.nhighest data.nlowest  

print('highest')
print(data.nlargest(5,'flow'))
print('smallest')
print(data.nsmallest(5,'flow'))

# %%
print(data.info())

# %%
# Using the groupby function to find highest and lowest values for each month 

print('highest flow for each month')

print(data.groupby('month')['flow'].nlargest(1))

print('lowest flow for each month')

print(data.groupby('month')['flow'].nsmallest(1))



 # %%
 # showing datetimes that are within 10% of my week one prediction
weekoneprediciton=60

data[(data["flow"] >= 54) & (data["flow"] <= 66)][["datetime","flow"]]

print(data[(data["flow"] >= 54) & (data["flow"] <= 66)][["datetime","flow"]])


# %%
# week 5! prediction script basing on last 7 days..keeping it simple 

p7 = data[["datetime","year", "month", "day","flow"]].tail(7)

p7

# %%
# looking at some hallmark values from this data to see where we are

print(p7.describe())



# %%
# looking at 10 lowest flows for each month to see where we are in relation to these values 
print(data.groupby('month')['flow'].nsmallest(10, keep='all'))


# %%
