# Starter code for Homework 4

# %%
# Import the modules we will use
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %%
# ** MODIFY **
# Set the file name and path to where you have stored the data
filename = 'streamflow_week4.txt'
filepath = os.path.join('../data', filename)
print(os.getcwd())
print(filepath)

# %%
# DON'T change this part -- this creates the lists you 
# should use for the rest of the assignment
# no need to worry about how this is being done now we will cover
# this in later sections. 

#Read the data into a pandas dataframe
data=pd.read_table(filepath, sep = '\t', skiprows=30,
        names=['agency_cd', 'site_no', 'datetime', 'flow', 'code']
        )

# Expand the dates to year month day
data[["year", "month", "day"]] =data["datetime"].str.split("-", expand=True)
data['year'] = data['year'].astype(int)
data['month'] = data['month'].astype(int)
data['day'] = data['day'].astype(int)

# Make a numpy array of this data
flow_data = data[['year', 'month','day', 'flow']].to_numpy()

# Getting rid of the pandas dataframe since we wont be using it this week
del(data)

# %%
# Starter Code
# Count the number of values with flow > 600 and month ==7
flow_count = np.sum((flow_data[:,3] > 600) & (flow_data[:,1]==7))

# this gives a list of T/F where the criteria are met
(flow_data[:,3] > 600) & (flow_data[:,1]==7)

# this give the flow values where that criteria is met
flow_pick = flow_data[(flow_data[:,3] > 600) & (flow_data[:,1]==7), 3]

# this give the year values where that criteria is met
year_pic = flow_data[(flow_data[:,3] > 600) & (flow_data[:,1]==7), 0]

# this give the all rows  where that criteria is met
all_pic = flow_data[(flow_data[:,3] > 600) & (flow_data[:,1]==7), ]

# Calculate the average flow for these same criteria 
flow_mean = np.mean(flow_data[(flow_data[:,3] > 600) & (flow_data[:,1]==7),3])

print("Flow meets this critera", flow_count, " times")
print('And has an average value of', flow_mean, "when this is true")

# Make a histogram of data
# Use the linspace  funciton to create a set  of evenly spaced bins
mybins = np.linspace(0, 1000, num=15)
# another example using the max flow to set the upper limit for the bins
#mybins = np.linspace(0, np.max(flow_data[:,3]), num=15) 
#Plotting the histogram
plt.hist(flow_data[:,3], bins = mybins)
plt.title('Streamflow')
plt.xlabel('Flow [cfs]')
plt.ylabel('Count')

# Get the quantiles of flow
# Two different approaches ---  you should get the same answer
# just using the flow column
flow_quants1 = np.quantile(flow_data[:,3], q=[0,0.1, 0.5, 0.9])
print('Method one flow quantiles:', flow_quants1)
# Or computing on a colum by column basis 
flow_quants2 = np.quantile(flow_data, q=[0,0.1, 0.5, 0.9], axis=0)
# and then just printing out the values for the flow column
print('Method two flow quantiles:', flow_quants2[:,3])
# %%

# %%

# Count the number of values with flow > 0 and month ==9
flow_count = np.sum((flow_data[:,3] > 0) & (flow_data[:,1]==9))

print('Days with flow greater 0 in September is', flow_count)


# %%
# Checking how many rows and Columns are in the data set "flow_data"
flow_data.shape



# Two different approaches ---  you should get the same answer
# just using the flow column

flow_quants1 = np.quantile(flow_data[:,3], q=[0,0.1, 0.5, 0.9])

# %%
## Looking closer at the flow trends for the END of Septmeber to make prediction
flow_mean_end = np.mean(flow_data[(flow_data[:,2]>=15) & (flow_data[:,1]==9) & (flow_data[:,0]>=2010),3])
print(flow_mean_end, "average flow for end of september 2010-present")
flow_mean_end5= np.mean(flow_data[(flow_data[:,2]>=15) & (flow_data[:,1]==9) & (flow_data[:,0]>=2015),3])
print(flow_mean_end5, "average flow from 2015-present")
flow_mean_end2019= np.mean(flow_data[(flow_data[:,2]>=15) & (flow_data[:,1]==9) & (flow_data[:,0]==2019),3])
print(flow_mean_end2019, "average 2019 End of september flows") 
# %%
# Make a histogram of data
# Use the linspace  funciton to create a set  of evenly spaced bins
mybins = np.linspace(0, 1000, num=15)
# another example using the max flow to set the upper limit for the bins
#mybins = np.linspace(0, np.max(flow_data[:,3]), num=15) 
#Plotting the histogram
flow_data_sep_all = flow_data[flow_data[:,1] ==9]
plt.hist(flow_data_sep_all[:,3], bins = mybins)
plt.title('September Streamflow 1989-Present')
plt.xlabel('Flow [cfs]')
plt.ylabel('Count')
# %%
# Make a histogram of data
# Use the linspace  funciton to create a set  of evenly spaced bins
mybins = np.linspace(0, 1000, num=15)
# another example using the max flow to set the upper limit for the bins
#mybins = np.linspace(0, np.max(flow_data[:,3]), num=15) 
#Plotting the histogram
flow_data_sep_end = flow_data[flow_data[:,1] ==9 & (flow_data[:,2]>=15)]
plt.hist(flow_data_sep_end[:,3], bins = mybins)
plt.title('End of September Streamflow 1989-Present')
plt.xlabel('Flow [cfs]')
plt.ylabel('Count')

# %%
# looking at quantiles to narrow down prediction from last five years 
flow_quants1 = np.quantile(flow_data[(flow_data[:,2]>=15) & (flow_data[:,1]==9) & (flow_data[:,0]>=2015),3], q=[0,0.1, 0.5, 0.9])
print(flow_quants1)

# %%
## Checking number of times verde has been above this value
flow_count = np.sum((flow_data[:,3] > 60) & (flow_data[:,1]==9))

print(flow_count)
a=946
# %%
## Checking total number days flow has been recorded in this data set 
flow_count = np.sum((flow_data[:,3] > 0) & (flow_data[:,1]==9))
print(flow_count)
# %%
#occurance as a percentage 
a=893
b=946
a/b *100 
# %%
# Homework question 1 
print(type(flow_data))


print(flow_data.dtype)

print(flow_data.ndim)

print(flow_data.shape)

print(flow_data.size)


# %%
##Looking at how prediciton was exceeded year <=2000, >=2010
flow_count1 = np.sum((flow_data[:,3] > 60) & (flow_data[:,1]==9) & (flow_data[:,0]<=2000))
print("number of times 60 cfs was exceeded before 2000=", flow_count1, "times")
flow_count2 = np.sum((flow_data[:,3] > 60) & (flow_data[:,1]==9) & (flow_data[:,0]>=2010))
print("number of times 60 cfs was exceeded after 2010=", flow_count2, "times")

a = flow_count1
b = flow_count2
c = 946

a/c *100

b/c *100


# %%
## Looking at daily flow differences between Beginning and End of september 
flow_mean_beg = np.mean(flow_data[(flow_data[:,2]<=15) & (flow_data[:,1]==9),3])
print(flow_mean_beg, "average flow for beginning of september")

flow_mean_end = np.mean(flow_data[(flow_data[:,2]>=15) & (flow_data[:,1]==9),3])
print(flow_mean_end, "average flow for end of september")

# %%
