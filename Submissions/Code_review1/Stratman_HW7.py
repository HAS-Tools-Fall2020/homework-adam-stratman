# Adam Stratman
# 10/9/20
# Code for code_review1


# %%
# Import the modules we will use
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import datetime


# Note you may need to do pip install for sklearn

# %%
# Building a function for flow prediction outside of the AR model
def real_prediction(indexnumber, last_week_flow, last2_week_flow=None):
    ''''
        This function is taking the linear regression prediction WITHOUT
        a factor to bring it down to a more reasonable value for the forecast
        of week 1.
        '''
    if indexnumber == 0 and last2_week_flow is None:
        rp = (model.intercept_ + model.coef_[indexnumber] * last_week_flow)
    if indexnumber == 1:
        rp = (model2.intercept_ + model2.coef_[0] * last_week_flow +
        model2.coef_[indexnumber] * last2_week_flow)
    if indexnumber != 0 and indexnumber != 1:
        print('The index number =', indexnumber, 'is not valid. Enter 0 or 1.')
        return rp


# %%
# ** MODIFY **
# Set the file name and path to where you have stored the data
filename = 'streamflow_week7.txt'
filepath = os.path.join('../../data', filename)
print(os.getcwd())
print(filepath)


# %%
# Read the data into a pandas dataframe
data = pd.read_table(filepath, sep='\t', skiprows=30,
       names=['agency_cd', 'site_no', 'datetime', 'flow', 'code'],
       parse_dates = ['datetime'])
# Expand the dates to year month day
data['year'] = pd.DatetimeIndex(data['datetime']).year
data['month'] = pd.DatetimeIndex(data['datetime']).month
data['day'] = pd.DatetimeIndex(data['datetime']).dayofweek
data['dayofweek'] = pd.DatetimeIndex(data['datetime']).dayofweek


# %%
# Aggregate flow values to weekly
flow_weekly = data.resample("W", on='datetime').mean()


# %%
# Setup 1: setting up the arrays for my model
# This is an autoregressive model that uses two time lags
flow_weekly['flow_tm1'] = flow_weekly['flow'].shift(1)
flow_weekly['flow_tm2'] = flow_weekly['flow'].shift(2)


# %%
# Setup 2)
# Here I'm grabbing the 370(year 1996)-600(year 2000) weeks
train = flow_weekly[370:600][['flow', 'flow_tm1', 'flow_tm2']]
test = flow_weekly[600:][['flow', 'flow_tm1', 'flow_tm2']]


# %%
# Making a linear regression with Sklearn
model = LinearRegression()
x=train['flow_tm1'].values.reshape(-1,1)
y=train['flow'].values
model.fit(x, y)
# Look at the results including r_squared value, intercept, slope
# r^2 values
r_sq = model.score(x,y)
print('coefficient of determination:', np.round(r_sq,2))
print('intercept:', np.round(model.intercept_, 2))
print('slope:', np.round(model.coef_, 2))


# %%
# 1) looking at one week time lag to make prediciton
# looking at prediction based on previous week 9/27-10/3
last_week_flow = 57.2
prediction = model.intercept_ + model.coef_ * last_week_flow
print("prediciton based on previous week=", prediction)


# %%
# 2) Doing the same thing as above but adding another week (week1, week 2 time lag)
# Using two time lags in the linear regression
model2 = LinearRegression()
x2=train[['flow_tm1','flow_tm2']]
model2.fit(x2, y)
r_sq = model2.score(x2, y)
print('coefficient of determination:', np.round(r_sq,2))
print('intercept:', np.round(model2.intercept_, 2))
print('slope:', np.round(model2.coef_, 2))


# %%
# 3) Using two weeks prior to make prediciton 9/20-9/26
last2_week_flow = 58.4
prediction2 = model2.intercept_ + model2.coef_[0] * last_week_flow + model2.coef_[1] * last2_week_flow
print("prediciton based on previous 2 weeks=", prediction2)


# %%
# Making my predictions outside of the AR model
my_prediction1 = real_prediction(0,last_week_flow)
my_prediction2 = real_prediction(1,last2_week_flow)


# %%
# The four numbers for this week are as follows
print("AR prediciton based on previous 1 week=", prediction.round(1))
print("AR prediciton based on previous 2 weeks=", prediction2.round(1))
<<<<<<< Updated upstream
print("Please use this number as my week 1 prediciton=", my_prediction1.round(1))
print("Please use this number as my week 2 prediciton=", my_prediction2.round(1))

# %%
# Alcely's recommendation
# Creating the function without a correction factor. This way you can use
# it in lines 93, 112, 118 and 119.


def real_prediction(indexnumber, last_week_flow, last2_week_flow=None):
    ''''
    This function is taking the linear regression prediction WITHOUT
    a factor to bring it down to a more reasonable value for the forecast
    of week 1.
    '''
    if indexnumber == 0 and last2_week_flow is None:
        rp = (model.intercept_ + model.coef_[indexnumber] * last_week_flow)
    if indexnumber == 1:
        rp = (model2.intercept_ + model2.coef_[0] * last_week_flow +
              model2.coef_[indexnumber] * last2_week_flow)
    if indexnumber != 0 and indexnumber != 1:
        print('The index number =', indexnumber, 'is not valid. Enter 0 or 1.')
    return rp

# %%
# testing Alcely's function


# apply the correction factor outside the function
prediction = real_prediction(1, 57.2, 58.4)*0.64
print(prediction.round(1))

# %%
=======
print("Please use this number as my week 1 prediciton=", (
      my_prediction1.round(1)))
print("Please use this number as my week 2 prediciton=", my_prediction2.round(1))
>>>>>>> Stashed changes
