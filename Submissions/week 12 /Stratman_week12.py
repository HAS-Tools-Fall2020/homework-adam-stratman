# Adam Stratman
# 11/17/20


# %%
# Import the modules we will use
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import os
import json
import urllib.request as req
import urllib
from sklearn.linear_model import LinearRegression
import xarray as xr
import rioxarray
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import seaborn as sns
import geopandas as gpd
import fiona
import shapely
from netCDF4 import Dataset
import matplotlib

# %%
# Building a function for flow prediction outside of the AR model
def real_prediction(indexnumber, last_week_flow, last2_week_flow=None):
    ''''
    This function is prepping the linear regression model to be
    multiplied by a correction factor to bring it down to a more
    reasonable value for the forecast of week 1 and week 2.
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
# reading in streamflow data from the internet

url = "https://waterdata.usgs.gov/nwis/dv?cb_00060=on&format=rdb&site_no=09506000&referred_module=sw&period=&begin_date=1989-01-01&end_date=2020-10-19"

# Now we can read it with read_table command the same as we did before
# Note this only works if you select the tab separated data --- try it with table and you will see it doesn't
data2 = pd.read_table(url, skiprows=30, names=['agency_cd', 'site_no',
                                               'datetime', 'flow', 'code'],
                      parse_dates=['datetime'], index_col='datetime')

#separating url onto multiple lines
url = "https://waterdata.usgs.gov/nwis/dv?cb_00060=on&format=rdb&site_no=09506000" \
      "&referred_module=sw&period=&begin_date=1989-01-01&end_date=2020-10-19"

#Replace parts of my url with variables
site = '09506000'
start = '1989-01-01'
end = '2020-10-31'
url = "https://waterdata.usgs.gov/nwis/dv?cb_00060=on&format=rdb&site_no=" + site + \
      "&referred_module=sw&period=&begin_date=" + start + "&end_date=" + end
data2 = pd.read_table(url, skiprows=30, names=['agency_cd', 'site_no',
                                               'datetime', 'flow', 'code'],
                      parse_dates=['datetime'], index_col='datetime')


# %%
# Read the data into a pandas dataframe
data = pd.read_table(url, sep='\t', skiprows=30,
                     names=['agency_cd', 'site_no', 'datetime', 'flow',
                            'code'],
                     parse_dates=['datetime'])
# Expand the dates to year month day
data['year'] = pd.DatetimeIndex(data['datetime']).year
data['month'] = pd.DatetimeIndex(data['datetime']).month
data['day'] = pd.DatetimeIndex(data['datetime']).dayofweek
data['dayofweek'] = pd.DatetimeIndex(data['datetime']).dayofweek

# %%
# Aggregate flow values to weekly
flow_weekly = data.resample("W", on='datetime').mean()
# %%
# Setting up the arrays for my model I will use
# This is an autoregressive model that uses two time lags
flow_weekly['flow_tm1'] = flow_weekly['flow'].shift(1)
flow_weekly['flow_tm2'] = flow_weekly['flow'].shift(2)
# %%
### # grabbing air temp for my Net CDF file historical time series
data_path = os.path.join('../data',
                         'daily_temp.nc')
# %%
# Read in the dataset as an x-array
dataset = xr.open_dataset(data_path)
# %%
# look at it
dataset

# %%
# We can inspect the metadata of the file like this:
metadata = dataset.attrs
metadata
# %%
# And we can grab out any part of it like this:
metadata['dataset_title']
# %%
# we can also look at other  attributes like this
dataset.values
dataset.dims
dataset.coords
# %%
# Focusing on just the air values
air = dataset['air']
air
# %%
# Now to grab out data first lets look at spatail coordinates:
dataset['air']['lat'].values.shape
# The first 4 lat values
dataset['air']['lat'].values
dataset['air']['lon'].values

# Now looking at the time;
dataset["air"]["time"].values
dataset["air"]["time"].values.shape

# %%
# Now lets take a slice: Grabbing data for just one point
lat = dataset["air"]["lat"].values[0]
lon = dataset["air"]["lon"].values[0]
print("Long, Lat values:", lon, lat)
one_point = dataset["air"].sel(lat=lat,lon=lon)
one_point.shape

# %%
#Convert to dataframe
one_point_df = one_point.to_dataframe()
one_point_df.head
# %%
# Pulling out an average of previous two weeks air temp to use in my ar model
two_wk_air = one_point_df.loc["2020-10-24":"2020-11-09"]
print(two_wk_air)

# %%
# Converting to imperial units

two_week_mean = two_wk_air["air"].mean()
print(two_week_mean)

kelvin_to_fahrenheit = (two_week_mean - 273.15) * 9/5 + 32

print(kelvin_to_fahrenheit)
# %%
# %%
# Variables that change weekly
last_week_flow = 126.571
last2_week_flow = 108.971
# %%
# Here I'm grabbing weeks from 1996-2000 as training dates
# For the test it runs from 2000 to most current time in data

# LC - You could think about having these date ranges be variable you
# define at the top
train = flow_weekly[370:600][['flow', 'flow_tm1', 'flow_tm2']]
test = flow_weekly[600:][['flow', 'flow_tm1', 'flow_tm2']]


# %%
# Making a linear regression with Sklearn
model = LinearRegression()
x = train['flow_tm1'].values.reshape(-1, 1)
y = train['flow'].values
model.fit(x, y)
# Look at the results including r_squared value, intercept, slope
# r^2 values
r_sq = model.score(x, y)
print('coefficient of determination:', np.round(r_sq, 2))
print('intercept:', np.round(model.intercept_, 2))
print('slope:', np.round(model.coef_, 2))


# %%
# Looking at one week time lag to make prediciton
# Looking at prediction based on previous week
prediction = model.intercept_ + model.coef_ * last_week_flow + ( kelvin_to_fahrenheit *model.coef_)*.5
print("prediciton based on previous week=", prediction)


# %%
# Adding another week to the model (week1, week 2 time lag)
# Using two time lags in the linear regression
model2 = LinearRegression()
x2 = train[['flow_tm1', 'flow_tm2']]
model2.fit(x2, y)
r_sq = model2.score(x2, y)
print('coefficient of determination:', np.round(r_sq, 2))
print('intercept:', np.round(model2.intercept_, 2))
print('slope:', np.round(model2.coef_, 2))
# %%
# Using two weeks prior to make prediciton 9/27-10/3
prediction2 = model2.intercept_ + model2.coef_[0] * last_week_flow
+ model2.coef_[1] * last2_week_flow + (kelvin_to_fahrenheit * model.coef_)*.5
print("prediciton based on previous 2 weeks=", prediction2)


# %%
# Making my predictions outside of the AR model
# This utilizes a correction factor calculated by looking at the AR model value
# And comparing it to previous weeks observed flow

my_prediction_1 = real_prediction(0, last_week_flow, None)*0.91
my_prediction_2 = real_prediction(1, last_week_flow, last2_week_flow)*.97
print("week 1 prediction outside AR=", my_prediction_1.round(1))
print("week 2 prediction outside AR=", my_prediction_2.round(1))


# %%
# The four numbers show my AR model and my corrected forecast values
# For week 1 and week 2 predicitons
print("AR prediciton based on previous 1 week=", prediction.round(1))
print("AR prediciton based on previous 2 weeks=", prediction2.round(1))
print("This is my week 1 prediction outside the AR model=",
      my_prediction_1.round(1))
print("This is my week 2 prediciton outside the AR model=",
      my_prediction_2.round(1))



# %%
# Redefining the data to be able to look at datetime
# Data easily and pull out times I want
data2 = data.copy()
data2['datetime'] = pd.to_datetime(data2['datetime'])
data2 = data2.set_index('datetime')


# %%
# Making a new data set to look at weekly minimum flows for 16 week forecast
data_w = data2.resample("w").min()


# %%
# Pulling out weekly data I will use for the 16 week forecast
data_w.loc["2019-8-15":"2019-12-15"]

# %%
# Here I have put the weekly data from the previous cell into an array
# I then averaged the current and proceeding week
weekly_2019_mins = np.array([48.1, 29.6, 35.7, 59, 48.6, 51.2, 60.9, 72.7,
                             80.7, 73.9, 81.2, 97.1, 124, 130, 147, 180, 445])

forecast_16_week = ((weekly_2019_mins +
                     np.roll(weekly_2019_mins, 1))/2.0)[1::1]
print("These will serve as my 16 week forecast values", forecast_16_week)


# %%
# Graph for NET CDF
# use x-array to plot timeseries
#one_point.plot.line()
#precip_val = one_point.values
# %%
# Make a nicer timeseries plot
f, ax = plt.subplots(figsize=(12, 6))
plt.style.use('dark_background')
one_point.plot.line(hue='lat',
                    marker=".",
                    ax=ax,
                    color="tab:grey", linewidth= 2.5,
                    markerfacecolor="darkseagreen", markersize= 10,
                    markeredgecolor="darkseagreen", alpha=.75)
plt.ylabel('Temperature (Kelvin)', fontsize=20)
plt.xlabel('Time', fontsize= 20)
matplotlib.rc('xtick', labelsize=10)
matplotlib.rc('ytick', labelsize=10)
ax.set(title="Time Series For a Single Lat / Lon Location")
# %%
