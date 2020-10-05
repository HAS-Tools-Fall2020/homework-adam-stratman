
# %%
# Import the modules we will use
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import datetime
#note you may need to do pip install for sklearn

# %%
# ** MODIFY **
# Set the file name and path to where you have stored the data
filename = 'streamflow_week6.txt'
filepath = os.path.join('../data', filename)
print(os.getcwd())
print(filepath)


# %%
#Read the data into a pandas dataframe
data=pd.read_table(filepath, sep = '\t', skiprows=30,
        names=['agency_cd', 'site_no', 'datetime', 'flow', 'code'],
        parse_dates=['datetime']
        )

# Expand the dates to year month day
data['year'] = pd.DatetimeIndex(data['datetime']).year
data['month'] = pd.DatetimeIndex(data['datetime']).month
data['day'] = pd.DatetimeIndex(data['datetime']).dayofweek
data['dayofweek'] = pd.DatetimeIndex(data['datetime']).dayofweek
# %%
# Aggregate flow values to weekly 
flow_weekly = data.resample("W", on='datetime').mean()
# %%
print(flow_weekly.iloc[[600]])


# %%
# Building an autoregressive model 
# You can learn more about the approach I'm following by walking 
# Through this tutorial
# https://realpython.com/linear-regression-in-python/

# Setup 1: setup the arrays you will build your model on
# This is an autoregressive model so we will be building
# it based on the lagged timeseries

flow_weekly['flow_tm1'] = flow_weekly['flow'].shift(1)
flow_weekly['flow_tm2'] = flow_weekly['flow'].shift(2)
flow_weekly['flow_tm3'] = flow_weekly['flow'].shift(3)

# Setup 2 - pick what portion of the time series you want to use as training data
# here I'm grabbing the 370(1996)-600(2000) weeks 
# Note1 - dropping the first two weeks since they wont have lagged data
# to go with them  
train = flow_weekly[370:600][['flow', 'flow_tm1', 'flow_tm2','flow_tm3']]
test = flow_weekly[600:][['flow', 'flow_tm1', 'flow_tm2', 'flow_tm3']]

# 1) Making a linear regression with Sklearn
model = LinearRegression()
x=train['flow_tm1'].values.reshape(-1,1) #See the tutorial to understand the reshape step here 
y=train['flow'].values
model.fit(x,y)

#Look at the results including r_squared value, intercept, slope
# r^2 values
r_sq = model.score(x, y)
print('coefficient of determination:', np.round(r_sq,2))
print('intercept:', np.round(model.intercept_, 2))
print('slope:', np.round(model.coef_, 2))

# looking at one week time lag as to make prediciton 
# %%
# looking at prediction based on previous week 9/27-10/3
last_week_flow = 57.3 
prediction = model.intercept_ + model.coef_ * last_week_flow
print("prediciton based on previous week=", prediction)

# 2) Doing the same thing as above but adding another week (week1, week 2 time lag
# %%
# Using two time lags in the linear regression 
model2 = LinearRegression()
x2=train[['flow_tm1','flow_tm2']]
model2.fit(x2,y)
r_sq = model2.score(x2, y)
print('coefficient of determination:', np.round(r_sq,2))
print('intercept:', np.round(model2.intercept_, 2))
print('slope:', np.round(model2.coef_, 2))

# Using two weeks prior to make prediciton 9/20-9/26
# %%
last2_week_flow = 58.2 
prediction2 = model2.intercept_ + model2.coef_[0] * last_week_flow + model2.coef_[1] * last2_week_flow
print("prediciton based on previous 2 weeks=", prediction2)

# 3) Making a final linear regression with three time lags in the model
 # %%
# Using three time lags in the linear regression 
model3 = LinearRegression()
x3=train[['flow_tm1','flow_tm2','flow_tm3']]
model3.fit(x3,y)
r_sq = model3.score(x3, y)
print('coefficient of determination:', np.round(r_sq,2))
print('intercept:', np.round(model3.intercept_, 2))
print('slope:', np.round(model3.coef_, 2))

# Using 3 weeks prior to make prediciton 9/13-9/19
# %%
last3_week_flow = 56.2
prediction3 = model3.intercept_ + model3.coef_[0] * last_week_flow + model3.coef_[1] * last2_week_flow + model3.coef_[2] * last3_week_flow
print("prediciton based on previous three weeks=", prediction3)
# %%
# 4) looking at the three predictions all together 
prediction = model.intercept_ + model.coef_ * last_week_flow
print("prediciton based on previous 1 week=", prediction)
print("prediciton based on previous 2 weeks=", prediction2)
print("prediciton based on previous 3 weeks=", prediction3)
# %% 

# 5) Making a plot of observed flow with training period 

plt.style.use('grayscale')
fig, ax = plt.subplots()
ax.set_facecolor('xkcd:silver')
ax.plot(flow_weekly['flow'], 'g', linewidth= 2 ,  label='full')
ax.plot(train['flow'], 'darkslategrey', linewidth=10 , label='training')
ax.plot(flow_weekly['flow'], 'aquamarine', label='observed flow', linewidth = 1)
ax.set(title="Observed Flow for 1996-2000", xlabel="Date", ylabel="Weekly Avg Flow [cfs]",
        yscale='log', xlim=[datetime.date(1996, 2, 4), datetime.date(2020, 10, 3)])
ax.legend()
plt.show()

fig.set_size_inches(5,3)
fig.savefig("ObservedFlow.png")


# %%
# 6) Line  plot comparison of predicted and observed flows
plt.style.use('grayscale')
ax.set_facecolor('xkcd:silver')
fig, ax = plt.subplots()
ax.plot(train['flow'], color='grey', linewidth=1, label='observed')
ax.plot(train.index, q_pred_train, 'darkslategrey', linestyle='--', linewidth=1, 
        label='simulated')
ax.set(title="Observed and Simulated flow", xlabel="Date", ylabel="Weekly Avg Flow [cfs]",
        yscale='log')
ax.legend()
fig.set_size_inches(5,3)
fig.savefig("Observed_simulated_Flow.png")

# %%
# 7) Scatter plot of t vs t-1 flow with log log axes
plt.style.use('grayscale')
ax.set_facecolor('xkcd:silver')
fig, ax = plt.subplots()
ax.scatter(train['flow_tm1'], train['flow'], marker='4',
              color='darkslategrey', label='obs')
ax.set(title="1 week lag with AR fit" , xlabel='flow t-1', ylabel='flow t', yscale='log', xscale='log')
ax.plot(np.sort(train['flow_tm1']), np.sort(q_pred_train), label='AR model')
ax.legend()
fig.set_size_inches(5,3)
fig.savefig("scatter_plott-1.png")



# %%
